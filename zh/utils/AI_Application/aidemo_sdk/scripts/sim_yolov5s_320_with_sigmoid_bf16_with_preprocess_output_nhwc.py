import os
import copy
import argparse
import numpy as np
import onnxruntime as ort
import nncase

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def cosine(gt, pred):
    return (gt @ pred) / (np.linalg.norm(gt, 2) * np.linalg.norm(pred, 2))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--onnx", type=str, help='original model file')
    parser.add_argument("--kmodel", type=str, help='kmodel file')
    args = parser.parse_args()

    # create simulator
    sim = nncase.Simulator()

    # read kmodel
    kmodel = read_model_file(args.kmodel)

    # load kmodel
    sim.load_model(kmodel)

    input_tensor=sim.get_input_tensor(0).to_numpy()
    input = np.random.randint(0, 256, input_tensor.shape, dtype=input_tensor.dtype)
    # cpu inference
    ort_session = ort.InferenceSession(args.onnx)
    input_name = ort_session.get_inputs()[0].name

    cpu_results = ort_session.run(None, {input_name : np.array(input / 255., 'float32')})

    # set input for simulator
    sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(input))

    # simulator inference
    nncase_results = []
    sim.run()
    for i in range(sim.outputs_size):
        nncase_result = sim.get_output_tensor(i).to_numpy()
        nncase_results.append(copy.deepcopy(nncase_result))


    # compare
    for i in range(sim.outputs_size):
        cos = cosine(np.reshape(nncase_results[i], (-1)), np.reshape(np.transpose(np.reshape(cpu_results[i], (255, -1)), [1, 0]), (-1)))
        print('output {0} cosine similarity : {1}'.format(i, cos))

if __name__ == '__main__':
    main()
