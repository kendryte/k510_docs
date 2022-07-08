![가나안 덮개.png](http://s2.loli.net/2022/03/30/7UG1IxrOXTo2QKw.png)

**<font face="黑体" size="6" style="float:right">K510 nncase 개발자 안내서</font>**

<font face="黑体"  size=3>문서 버전: V1.0.1</font>

<font face="黑体"  size=3>게시 날짜: 2022-05-10</font>

<div style="page-break-after:always"></div>

<font face="黑体" size=3>**면책 조항**</font>
귀하가 구매한 제품, 서비스 또는 기능은 베이징 Jiananges 정보 기술 유한 회사(이하 "회사")의 상업 계약 및 약관의 적용을 받으며, 이 문서에 설명된 제품, 서비스 또는 기능의 전부 또는 일부는 구매 또는 사용의 범위를 벗어납니다. 계약에 달리 합의하지 않는 한, 회사는 본 문서의 진술, 정보, 내용의 정확성, 신뢰성, 완전성, 마케팅, 특정 목적 및 비침략성에 대해 명시적 또는 묵시적으로 어떠한 진술이나 보증도 하지 않습니다. 달리 합의하지 않는 한, 이 문서는 사용 지침의 참조로만 사용됩니다.
이 문서의 내용은 제품 버전 업그레이드 또는 기타 이유로 인해 예고 없이 수시로 업데이트되거나 수정될 수 있습니다. 

**<font face="黑体"  size=3>상표 고지</font>**

베이징 <img src="http://s2.loli.net/2022/03/30/xN21jbhnwSFyGRD.png" style="zoom:33%;" />Jianan Jets 정보 기술 유한 공사의 상표는 Jianan, Jianan 및 Jianan의 다른 상표입니다. 이 문서에 언급될 수 있는 기타 모든 상표 또는 등록 상표는 해당 소유자가 소유합니다. 

**<font face="黑体"  size=3>저작권 ©2022 베이징 Jiananjets 정보 기술 유한 회사</font>**
이 문서는 K510 플랫폼 개발 및 설계에만 적용되며, 어떠한 단위나 개인도 회사의 서면 허가 없이 이 문서의 일부 또는 전부를 어떤 형태로든 배포할 수 없습니다. 

**<font face="黑体"  size=3>베이징 Jiananjets 정보 기술 유한 회사</font>**
웹 사이트: canaan-creative.com
비즈니스 문의: salesAI@canaan-creative.com

<div style="page-break-after:always"></div>
# 서문
**<font face="黑体"  size=5>문서의 목적</font>**
이 문서는 nncase/K510 compiler에 대한 사용 설명서로, 사용자에게 nncase를 설치하는 방법, 신경망 모델을 컴파일하기 위해 compiler API를 호출하는 방법 및 runtime API가 AI 추론 프로그램을 작성하는 방법을 제공합니다

**<font face="黑体"  size=5>독자 개체입니다</font>**

이 문서(이 가이드)가 주로 적용되는 사람:

- 소프트웨어 개발자
- 기술 지원 담당자

**<font face="黑体"  size=5>용어 및 약어</font>**

| 용어입니다 | 설명/전체 이름입니다                              |
| ---- | -------------------------------------- |
| 증권 시세 표시기  | Post-training quantization, 트레이닝 후 정량화 |
| 증권 시세 표시기  | mean-square error, 평균 제곱 오차            |
|      |                                        |

**<font face="黑体"  size=5>레코드를 수정합니다</font>**
 <font face="宋体"  size=2>개정 레코드에는 각 문서 업데이트에 대한 설명이 누적됩니다. 문서의 최신 버전에는 이전 버전의 모든 업데이트가 포함되어 있습니다. </font>

| 버전 번호입니다   | 수정자     | 개정일입니다 | 개정 지침 |
|  :-----  |-------   |  ------  |  ------  |
| V1.0.1 | 장양하다 | 2022-05-10 | nncase_v1.6.1 |
| V1.0.0 | 장양/ 장제자오/ 양하오치 | 2022-05-06 | nncase_v1.6.0 |
| V0.9.0 | 장양하다 | 2022-04-01 | nncase_v1.5.0 |
| V0.8.0 | 장양 | 2022-03-03 | nncase_v1.4.0 |
| V0.7.0 | 장양하다 | 2022-01-28 | nncase_v1.3.0 |
| V0.6.0 | 장양하다 | 2021-12-31 | nncase_v1.2.0 |
| V0.5.0 | 장양하다 | 2021-12-03 | nncase_v1.1.0 |
| V0.4.0 | 장양/ 양하오치 / 정치항 | 2021-10-29 | nncase_v1.0.0 |
| V0.3.0 | 장양 | 2021-09-28 | nncase_v1.0.0_rc1 |
| V0.2.0 | 장양 | 2021-09-02 | nncase_v1.0.0_베타2 |
| V0.1.0 | 장양 | 2021-08-31 | nncase_v1.0.0_베타1 |

<div style="page-break-after:always"></div>
**<font face="黑体"  size=6>카탈로그</font>**

[목차]

<div style="page-break-after:always"></div>

# 1 개발 환경에 대한 간략한 소개

## 1.1 운영 체제

- 우분투 18.04/20.04

## 1.2 소프트웨어 환경

소프트웨어 환경 요구 사항은 다음 표에 나와 있습니다.

| 일련 번호입니다 | 소프트웨어 리소스        | 설명합니다                        |
| ---- | --------------- | --------------------------- |
| 1    | 파이썬          | 파이썬 3.6/3.7/3.8/3.9/3.10 |
| 2    | 핍3            | pip3 버전 > = 20.3            |
| 3    | onnx            | onnx 버전은 1.9.0입니다             |
| 4    | onnx 단순화 | onnx-simplifier 버전은 0.3.6입니다  |
| 5    | onnxoptimizer   | onnxoptimizer 버전은 0.2.6입니다    |

## 1.3 하드웨어 환경

하드웨어 환경 요구 사항은 다음 표에 나와 있습니다.

| 일련 번호입니다 | 하드웨어 리소스입니다     | 설명합니다 |
| ---- | ------------ | ---- |
| 1    | K510 CRB     |      |
| 2    | SD 카드 및 카드 리더기 |      |

# 2 nncase 소개

## 2.1 nncase란 무엇입니까?

nncase는 AI 가속기를 위해 설계된 신경망 컴파일러이며 현재 cpu/K210/K510 등을 지원하는 target을 지원합니다

nncase에서 제공하는 기능입니다

- 다중 입력 다중 출력 네트워크 및 다중 분기 구조를 지원합니다
- 정적 메모리 할당, 힙 메모리가 필요하지 않습니다
- 연산자 병합 및 최적화
- float 및 uint8/int8 정량적 추론을 지원합니다
- 부동 소수점 모델 및 양자화 보정 집합을 사용하여 학습 후 양자화를 지원합니다
- 0 복사 로드를 지원하는 플랫 모델입니다

nncase에서 지원하는 신경망 프레임워크입니다

- tflite
- onnx
- 카페

## 2.2 제품 이점

- **간단한 종단 간 배포**

  사용자와 상호 작용하는 횟수를 줄입니다. 사용자가 CPU, GPU 모델을 사용하고 배포하는 것과 동일한 도구와 프로세스를 사용하면 KPU에 배포할 수 있습니다. 복잡한 매개 변수를 설정하고, 사용 임계값을 낮추고, AI 알고리즘의 반복 주기를 가속화할 필요가 없습니다.
- **기존 AI 생태계를 최대한 활용한다**

  업계에서 널리 사용되는 프레임워크에 부착되어 있습니다. 한편으로는 가시성을 높이고 성숙한 생태의 배당금을 누릴 수 있습니다. 다른 한편으로는, 중소 개발자의 개발 비용을 줄일 수 있습니다, 업계에서 성숙한 모델과 알고리즘은 직접 배포 할 수 있습니다.
- **하드웨어 성능을 최대한 활용하십시오**

  NPU의 장점은 CPU, GPU보다 성능이 높기 때문에 DL Compiler는 하드웨어 성능을 최대한 활용할 수 있어야 합니다. 또한 Compiler는 새로운 모델 구조에 맞게 성능을 최적화해야 하므로 수동 최적화를 넘어 새로운 자동 최적화 기술을 탐색해야 합니다.
- **확장성 및 서비스 용이성**

  K210, K510 및 향후 칩의 AI 모델 배포를 지원할 수 있습니다. 아키텍처 수준에서 확장성을 제공해야 합니다. 새 Target을 추가하는 데 드는 비용은 최소화되며 가능한 한 많은 모듈을 재사용할 수 있습니다. DL Compiler의 기술 축적을 위해 신제품 개발을 가속화합니다.

## 2.3 nncase 스키마입니다

<img src="https://i.loli.net/2021/08/18/IQR12SOJdzxTUZH.png" alt="nncase_arch.png" style="zoom:67%;" />

nnncase 소프트웨어 스택은 현재 compiler 및 runtime 섹션으로 구성됩니다.

**Compiler:** PC에서 신경망 모델을 컴파일하여 궁극적으로 kmodel 파일을 생성하는 데 사용됩니다. 주로 importer, IR, Evaluator, Quantize, Transform 최적화, Tiling, Partition, Schedule, Codegen 등의 모듈이 있습니다. 

- Importer: 다른 신경망 프레임워크의 모델을 nncase로 가져옵니다
- IR: 중간 표현은 importer에서 가져온 Neutral IR(장치 독립적)과 Neutral IR의 로버링 변환에 의해 생성된 Target IR(장치 종속)으로 나뉩니다.
- Evaluator: Evaluator는 Constant Folding/PTQ Calibration과 같은 시나리오에서 자주 사용되는 IR의 해석 실행 기능을 제공합니다
- Transform: IR 변환 및 그래프에 대한 트래버스 최적화 등
- Quantize: 학습 후 양자화, 정량화할 tensor에 양자화 마커 추가, 입력 보정 집합에 따라 해석 실행을 위해 Evaluator 호출, tensor의 데이터 범위 수집, 양자화/반정량 노드 삽입, 마지막으로 불필요한 양자화/반정량적 노드 제거 최적화 등
- Tiling: NPU의 낮은 메모리 용량으로 인해 큰 블록 계산을 분할해야 합니다. 또한 계산에 많은 양의 데이터가 멀티플렉싱될 때 Tiling 매개 변수를 선택하면 대기 시간 및 대역폭에 영향을 줄 수 있습니다
- Partition: 그래프를 ModuleType으로 분할하고 각 하위 그래프는 RuntimeModule에 해당하고 다른 유형의 RuntimeModule은 다른 Device(cpu/K510)에 해당합니다.
- Schedule: 최적화된 그래프의 데이터 종속성을 기반으로 계산 순서를 생성하고 Buffer를 할당합니다
- Codegen: 각 서브플레인에 대해 ModuleType에 해당하는 코드gen을 호출하여 RuntimeModule을 생성합니다

**Runtime**: 사용자 앱에 통합되어 kmodel/설정 입력 데이터/KPU 실행/출력 데이터 가져오기와 같은 기능을 제공합니다

# 3 nncase를 설치합니다

nncase 툴체인 compiler 섹션에는 nncase 및 K510 compiler가 포함되어 있으며, 모두 해당 wheel 패키지를 설치해야 합니다.

- nncase wheel 패키지는[ nncase github에 ](https://github.com/kendryte/nncase/releases/tag/v1.6.0)출시되며 Python 3.6/3.7/3.8/3.9/3.10을 지원하며 사용자는 운영 체제 및 Python에 따라 적절한 버전을 선택하여 다운로드할 수 있습니다
- K510 compiler wheel 패키지는 nncase sdk의 x86_64 디렉토리에 있으며 Python 버전에 의존하지 않고 직접 설치할 수 있습니다

우분투 환경이 없는 사용자는 [nncase docker](https://github.com/kendryte/nncase/blob/master/docs/build.md#docker)(Ubuntu 20.04 + Python 3.8)를 사용할 수 있습니다

```shell
cd /path/to/nncase_sdk
docker pull registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest
docker run -it --rm -v `pwd`:/mnt -w /mnt registry.cn-hangzhou.aliyuncs.com/kendryte/nncase:latest /bin/bash -c "/bin/bash"
```

우분투 20.04 + 파이썬 3.8 설치nncase를 예로 들어 보겠습니다

```shell
wget -P x86_64 https://github.com/kendryte/nncase/releases/download/v1.6.0/nncase-1.6.0.20220505-cp38-cp38-manylinux_2_24_x86_64.whl
pip3 install x86_64/*.whl
```
<!-- markdownlint-disable no-emphasis-as-header -->
# 4 컴파일/추론 모델

nncase는 **PC에서 딥 러닝 모델을 컴파일/추론하기 위한** Python API s를 제공합니다

## 4.1 지원되는 연산자입니다

### 4.1.1 tflite 연산자

| 연산자                | 지원 됨 |
| ----------------------- | ------------ |
| 아 BS                     | ✅            |
| 더하다                     | ✅            |
| ARG_MAX                 | ✅            |
| ARG_MIN                 | ✅            |
| AVERAGE_POOL_2D         | ✅            |
| BATCH_MATMUL            | ✅            |
| 캐스트                    | ✅            |
| 세일                    | ✅            |
| 연결           | ✅            |
| CONV_2D                 | ✅            |
| 몸                     | ✅            |
| 관습                  | ✅            |
| DEPTHWISE_CONV_2D       | ✅            |
| 증권 시세 표시기                     | ✅            |
| 같다                   | ✅            |
| 특급                     | ✅            |
| EXPAND_DIMS             | ✅            |
| 층                   | ✅            |
| FLOOR_DIV               | ✅            |
| FLOOR_MOD               | ✅            |
| FULLY_CONNECTED         | ✅            |
| 큰                 | ✅            |
| GREATER_EQUAL           | ✅            |
| L2_NORMALIZATION        | ✅            |
| LEAKY_RELU              | ✅            |
| 덜                    | ✅            |
| LESS_EQUAL              | ✅            |
| 로그                     | ✅            |
| 로지스틱                | ✅            |
| MAX_POOL_2D             | ✅            |
| 최대                 | ✅            |
| 의미하다                    | ✅            |
| 최소                 | ✅            |
| 나는                     | ✅            |
| 네그                     | ✅            |
| NOT_EQUAL               | ✅            |
| 패드                     | ✅            |
| 패드브2                   | ✅            |
| MIRROR_PAD              | ✅            |
| 팩                    | ✅            |
| 포로                     | ✅            |
| REDUCE_MAX              | ✅            |
| REDUCE_MIN              | ✅            |
| REDUCE_PROD             | ✅            |
| 렐루                    | ✅            |
| 프렐루                   | ✅            |
| 렐루6                   | ✅            |
| 바꿀                 | ✅            |
| RESIZE_BILINEAR         | ✅            |
| RESIZE_NEAREST_NEIGHBOR | ✅            |
| 둥근                   | ✅            |
| RSQRT                   | ✅            |
| 모양                   | ✅            |
| 없이                     | ✅            |
| 부분                   | ✅            |
| 소프트맥스                 | ✅            |
| SPACE_TO_BATCH_ND       | ✅            |
| 짜다                 | ✅            |
| BATCH_TO_SPACE_ND       | ✅            |
| STRIDED_SLICE           | ✅            |
| 증권 시세 표시기                    | ✅            |
| 정사각형                  | ✅            |
| 하위                     | ✅            |
| 합계                     | ✅            |
| 물고기                    | ✅            |
| 타일                    | ✅            |
| 바꾸어               | ✅            |
| TRANSPOSE_CONV          | ✅            |
| 양자화                | ✅            |
| FAKE_QUANT              | ✅            |
| 양자화 해제              | ✅            |
| 모으다                  | ✅            |
| GATHER_ND               | ✅            |
| ONE_HOT                 | ✅            |
| SQUARED_DIFFERENCE      | ✅            |
| LOG_SOFTMAX             | ✅            |
| 쪼개다                   | ✅            |
| HARD_SWISH              | ✅            |

### 4.1.2 onnx 연산자

| 연산자              | 지원 됨 |
| --------------------- | ------------ |
| 아 bs                   | ✅            |
| 아코스                  | ✅            |
| 아코쉬                 | ✅            |
| 그리고                   | ✅            |
| 아르그맥스                | ✅            |
| 아르그민                | ✅            |
| 짠                  | ✅            |
| 아신                 | ✅            |
| 더하다                   | ✅            |
| 평균풀           | ✅            |
| 배치 정규화    | ✅            |
| 캐스트                  | ✅            |
| 세일                  | ✅            |
| 받는 사람                  | ✅            |
| 클립                  | ✅            |
| 콘캣                | ✅            |
| 상수              | ✅            |
| 상수형모양       | ✅            |
| 컨벤션                  | ✅            |
| ConvTranspose         | ✅            |
| 몸                   | ✅            |
| 코쉬                  | ✅            |
| 컴섬                | ✅            |
| 깊이공간          | ✅            |
| 디퀀티제이니어      | ✅            |
| div                   | ✅            |
| 드롭아웃               | ✅            |
| 생명                   | ✅            |
| 특급                   | ✅            |
| 넓히다                | ✅            |
| 같다                 | ✅            |
| 평평               | ✅            |
| 층                 | ✅            |
| 모으다                | ✅            |
| GatherND              | ✅            |
| 젬                  | ✅            |
| 글로벌평균풀     | ✅            |
| 글로벌맥스풀         | ✅            |
| 큰               | ✅            |
| GreaterOrEqual        | ✅            |
| 하드맥스               | ✅            |
| 하드시그모이드           | ✅            |
| 하드스위시             | ✅            |
| 신원              | ✅            |
| 인스턴스정규화 | ✅            |
| LpNormalization       | ✅            |
| 리키렐루             | ✅            |
| 덜                  | ✅            |
| LessOrEqual           | ✅            |
| 로그                   | ✅            |
| 로그소프트맥스            | ✅            |
| 증권 시세 표시기                   | ✅            |
| 증권 시세 표시기                  | ✅            |
| 마트멀                | ✅            |
| 맥스풀               | ✅            |
| 최대                   | ✅            |
| 분                   | ✅            |
| 나는                   | ✅            |
| 네그                   | ✅            |
| 안                   | ✅            |
| 원핫                | ✅            |
| 패드                   | ✅            |
| 포로                   | ✅            |
| 프렐루                 | ✅            |
| 양자화선형        | ✅            |
| 랜덤노멀          | ✅            |
| 랜덤노멀라이즈      | ✅            |
| 랜덤 유니폼         | ✅            |
| 랜덤 유니폼처럼     | ✅            |
| 감소L1              | ✅            |
| 감소L2              | ✅            |
| 감소로그합계          | ✅            |
| ReduceLogSumExp       | ✅            |
| 감소맥스             | ✅            |
| 감소평균(ReduceMean)            | ✅            |
| 감소민             | ✅            |
| 감소 프로드            | ✅            |
| 감소합계             | ✅            |
| ReduceSumSquare       | ✅            |
| 렐루                  | ✅            |
| 바꿀               | ✅            |
| 크기 조정                | ✅            |
| 역시퀀스       | ✅            |
| 로이 얼라인(RoiAlign)              | ✅            |
| 둥근                 | ✅            |
| 마을                  | ✅            |
| 모양                 | ✅            |
| 기호                  | ✅            |
| 없이                   | ✅            |
| 출생                  | ✅            |
| 시그모이드               | ✅            |
| 크기                  | ✅            |
| 부분                 | ✅            |
| 소프트맥스               | ✅            |
| 소프트플러스              | ✅            |
| 소프트사인              | ✅            |
| 스페이스투뎁스          | ✅            |
| 쪼개다                 | ✅            |
| 스퀘어 르트                  | ✅            |
| 짜다               | ✅            |
| 하위                   | ✅            |
| 합계                   | ✅            |
| 물고기                  | ✅            |
| 타일                  | ✅            |
| 톱케이                  | ✅            |
| 바꾸어             | ✅            |
| 트릴루                 | ✅            |
| 업샘플링              | ✅            |
| 짜내기             | ✅            |
| 어디                 | ✅            |

### 4.1.3 caffe 연산자

| 연산자              | 지원 됨 |
| --------------------- | ------------ |
| 입력                 | ✅            |
| 콘캣                | ✅            |
| 회선           | ✅            |
| 엘트와이즈               | ✅            |
| 트레이드 인               | ✅            |
| 렐루                  | ✅            |
| 바꿀               | ✅            |
| 부분                 | ✅            |
| 소프트맥스               | ✅            |
| 쪼개다                 | ✅            |
| 연속 표시기 | ✅            |
| 풀링               | ✅            |
| 배치 표준             | ✅            |
| 저울                 | ✅            |
| 후진               | ✅            |
| 증권 시세 표시기                  | ✅            |
| 내부 제품          | ✅            |

## 4.2 모델 API를 컴파일합니다

현재 컴파일된 모델 API는 tflite/onnx/caffe와 같은 딥 러닝 프레임워크를 지원합니다.

### 4.2.1 컴파일 옵션

**기능에 대한 설명입니다**

nncase 컴파일 옵션을 구성하는 CompileOptions 클래스입니다

**클래스 정의입니다**

```python
py::class_<compile_options>(m, "CompileOptions")
    .def(py::init())
    .def_readwrite("target", &compile_options::target)
    .def_readwrite("quant_type", &compile_options::quant_type)
    .def_readwrite("w_quant_type", &compile_options::w_quant_type)
    .def_readwrite("use_mse_quant_w", &compile_options::use_mse_quant_w)
    .def_readwrite("split_w_to_act", &compile_options::split_w_to_act)
    .def_readwrite("preprocess", &compile_options::preprocess)
    .def_readwrite("swapRB", &compile_options::swapRB)
    .def_readwrite("mean", &compile_options::mean)
    .def_readwrite("std", &compile_options::std)
    .def_readwrite("input_range", &compile_options::input_range)
    .def_readwrite("output_range", &compile_options::output_range)
    .def_readwrite("input_shape", &compile_options::input_shape)
    .def_readwrite("letterbox_value", &compile_options::letterbox_value)
    .def_readwrite("input_type", &compile_options::input_type)
    .def_readwrite("output_type", &compile_options::output_type)
    .def_readwrite("input_layout", &compile_options::input_layout)
    .def_readwrite("output_layout", &compile_options::output_layout)
    .def_readwrite("model_layout", &compile_options::model_layout)
    .def_readwrite("is_fpga", &compile_options::is_fpga)
    .def_readwrite("dump_ir", &compile_options::dump_ir)
    .def_readwrite("dump_asm", &compile_options::dump_asm)
    .def_readwrite("dump_quant_error", &compile_options::dump_quant_error)
    .def_readwrite("dump_dir", &compile_options::dump_dir)
    .def_readwrite("benchmark_only", &compile_options::benchmark_only);
```

각 속성은 아래에 설명되어 있습니다

| 속성 이름입니다         | 형식입니다   | 필요한지 여부 | 설명입니다                                                         |
| ---------------- | ------ | -------- | ------------------------------------------------------------ |
| 과녁           | 문자열 | 네       | 컴파일 대상 지정(예: 'k210', 'k510'                               |
| quant_type       | 문자열 | 아니요, 그렇지 않습니다       | 데이터 양자화 유형 지정(예: 'uint8', 'int8'                          |
| w_quant_type     | 문자열 | 아니요, 그렇지 않습니다       | 가중치 양자화 유형(예: 'uint8', 'int8', 기본값 'uint8')을 지정합니다.           |
| use_mse_quant_w  | 부울   | 아니요, 그렇지 않습니다       | 가중치 양자화를 위해 평균 제곱 오차 최소화(mean-square error, MSE) 알고리즘을 사용하여 양자화 매개변수를 최적화할지 여부를 지정합니다 |
| split_w_to_act   | 부울   | 아니요, 그렇지 않습니다       | 가중치 데이터의 일부를 활성 데이터로 균형 조정할지 여부를 지정합니다                       |
| 전처리       | 부울   | 아니요, 그렇지 않습니다       | 전처리를 켤지 여부는 기본적으로 False로 설정됩니다                                  |
| 스왑RB           | 부울   | 아니요, 그렇지 않습니다       | RGB 입력 데이터의 빨간색과 파란색 채널(RGB->BGR 또는 BGR->RGB)을 교환할지 여부는 기본적으로 False로 설정됩니다 |
| 의미하다             | 목록   | 아니요, 그렇지 않습니다       | 선행 처리 정규화된 매개변수 평균( 기본값)입니다[0, 0, 0]                        |
| 성병              | 목록   | 아니요, 그렇지 않습니다       | 정규화된 매개변수 분산을 선행 처리합니다( 기본값은 )[1, 1, 1]                        |
| input_range      | 목록   | 아니요, 그렇지 않습니다       | 데이터 반전 후 해당 부동 소수점 숫자의 범위를 입력합니다(기본값)[0，1]               |
| output_range     | 목록   | 아니요, 그렇지 않습니다       | 고정 소수점 데이터를 내보내기 전에 부동 소수점 숫자의 범위에 해당하며 기본값은 비어 있습니다                     |
| input_shape      | 목록   | 아니요, 그렇지 않습니다       | 입력 데이터의 shape를 지정하고, input_shape layout은 input layout과 일치해야 하며, 입력 데이터의 input_shape 모델의 input shape와 일치하지 않을 때 leterbox 작업(resize/pad 등)을 수행합니다. |
| letterbox_value  | 뜨다  | 아니요, 그렇지 않습니다       | 선행 처리 letterbox의 채우기 값을 지정합니다                                  |
| input_type       | 문자열 | 아니요, 그렇지 않습니다       | 입력 데이터 유형을 지정합니다. 기본값은 'float32'입니다.                          |
| output_type      | 문자열 | 아니요, 그렇지 않습니다       | 출력 데이터 유형(예: 'float32', 'uint8'(양자화만 해당)을 지정합니다. 기본값은 'float32'입니다. |
| input_layout     | 문자열 | 아니요, 그렇지 않습니다       | 'NCHW', 'NHWC'와 같은 입력 데이터를 지정합니다. 데이터 layout을 가져오는 것이 모델 자체의 layout과 다른 경우 nncase는 transpose를 삽입하여 변환합니다 |
| output_layout    | 문자열 | 아니요, 그렇지 않습니다       | 'NCHW', 'NHWC'와 같은 출력 데이터를 지정하는 layout. 출력 데이터 layout이 모델 자체 layout과 다른 경우 nncase는 transpose를 삽입하여 변환합니다 |
| model_layout     | 문자열 | 아니요, 그렇지 않습니다       | 모델의 layout을 지정하고 기본값은 비어 있으며, tflite 모델 layout이 'NCHW'이고 Onnx 및 Caffe 모델 layout이 'NHWC'인 경우 지정합니다 |
| is_fpga          | 부울   | 아니요, 그렇지 않습니다       | kmodel이 fpga에 사용되는지 여부를 지정합니다( 기본값은 False)                          |
| dump_ir          | 부울   | 아니요, 그렇지 않습니다       | dump IR인지 여부를 지정합니다( 기본값은 False)                                 |
| dump_asm         | 부울   | 아니요, 그렇지 않습니다       | 파일을 dump asm으로 어셈블할지 여부를 지정합니다( 기본값은 False)                        |
| dump_quant_error | 부울   | 아니요, 그렇지 않습니다       | 덤프 정량화 전후의 모델 오류를 지정합니다                               |
| dump_dir         | 문자열 | 아니요, 그렇지 않습니다       | 앞에서 dump_ir 등의 스위치를 지정한 후 여기서 dump의 디렉터리를 지정합니다. 기본값은 빈 문자열입니다  |
| benchmark_only   | 부울   | 아니요, 그렇지 않습니다       | kmodel이 benchmark에만 사용할지 여부를 지정합니다( 기본값은 False)                   |

> 1. input range는 부동 소수점 숫자의 범위, 즉 입력 데이터 형식이 uint8인 경우 input range는 부동 소수점 뒤에 역정량화된 범위입니다(0~1이 아님).
> 2. input_shape input_layout 따라 지정해야 합니다([1，224，224，3]예: input_layout NCHW인 경우 input_shape 지정해야 함[1,3,224,224]). input_layout NHWC인 경우 input_shape 지정해야 합니다[1,224,224,3]. 
> 3. mean 및 std는 부동 소수점 숫자에 대한 normalize 매개 변수를 수행하며 사용자는 자유롭게 지정할 수 있습니다.
> 4. letterbox 기능을 사용하는 경우 1.5MB 이내의 입력 size, 0.75MB의 단일channel size를 제한해야 합니다.
>
> 예를 들면 다음과 같습니다.
>
> 1. 입력 데이터 형식은 uint8로 설정되고 input_range 설정되며[0,255], 반정량화의 역할은 형식 변환일 뿐이며, uint8의 데이터를 float32로 변환하고, mean 및 std 매개 변수는 여전히 0~255의 데이터에 따라 지정할 수 있습니다
> 2. 입력 데이터 형식이 uint8로 설정되고 input_range 고정 [0,1]소수점 숫자가 범위의 부동 소수점 숫자로 역정량화되고[0,1] mean 및 std는 새 부동 소수점 숫자 범위에 따라 지정해야 합니다. 

선행 처리 프로세스는 다음과 같습니다(그림의 녹색 노드는 선택 사항임).

![전처리.png](https://i.loli.net/2021/11/08/fhBLsozUTCbt4dp.png)

**코드 샘플입니다**

CompileOptions를 인스턴스화하고 각 속성의 값을 구성합니다

```python
# compile_options
compile_options = nncase.CompileOptions()
compile_options.target = target
compile_options.input_type = 'float32'  # or 'uint8' 'int8'
compile_options.output_type = 'float32'  # or 'uint8' 'int8'. Only work in PTQ
compile_options.output_range = []  # Only work in PTQ and output type is not "float32"
compile_options.preprocess = True # if False, the args below will unworked
compile_options.swapRB = True
compile_options.input_shape = [1,224,224,3] # keep layout same as input layout
compile_options.input_layout = 'NHWC'
compile_options.output_layout = 'NHWC'
compile_options.model_layout = '' # Specific it when tflite model with "NCHW" layout and Onnx(Caffe) model with "NHWC" layout
compile_options.mean = [0,0,0]
compile_options.std = [1,1,1]
compile_options.input_range = [0,1]
compile_options.letterbox_value = 114. # pad what you want
compile_options.dump_ir = True
compile_options.dump_asm = True
compile_options.dump_dir = 'tmp'
```

### 4.2.2 가져오기 옵션

**기능에 대한 설명입니다**

nncase 가져오기 옵션을 구성하는 ImportOptions 클래스입니다

**클래스 정의입니다**

```python
py::class_<import_options>(m, "ImportOptions")
    .def(py::init())
    .def_readwrite("output_arrays", &import_options::output_arrays);
```

각 속성은 아래에 설명되어 있습니다

| 속성 이름입니다      | 형식입니다   | 필요한지 여부 | 설명입니다     |
| ------------- | ------ | -------- | -------- |
| output_arrays | 문자열 | 아니요, 그렇지 않습니다       | 출력 이름입니다 |

**코드 샘플입니다**

ImportOptions를 인스턴스화하고 각 속성의 값을 구성합니다

```python
# import_options
import_options = nncase.ImportOptions()
import_options.output_arrays = 'output' # Your output node name
```

### 4.2.3 PTQTensor옵션

**기능에 대한 설명입니다**

ptQTensorOptions 클래스로 nncase PTQ 옵션을 구성합니다

**클래스 정의입니다**

```python
py::class_<ptq_tensor_options>(m, "PTQTensorOptions")
    .def(py::init())
    .def_readwrite("calibrate_method", &ptq_tensor_options::calibrate_method)
    .def_readwrite("samples_count", &ptq_tensor_options::samples_count)
    .def("set_tensor_data", [](ptq_tensor_options &o, py::bytes bytes) {
        uint8_t *buffer;
        py::ssize_t length;
        if (PyBytes_AsStringAndSize(bytes.ptr(), reinterpret_cast<char **>(&buffer), &length))
            throw std::invalid_argument("Invalid bytes");
        o.tensor_data.assign(buffer, buffer + length);
    });
```

각 속성은 아래에 설명되어 있습니다

| 필드 이름입니다         | 형식입니다   | 필요한지 여부 | 설명입니다                                                                                  |
| ---------------- | ------ | -------- | ------------------------------------------------------------------------------------- |
| calibrate_method | 문자열 | 아니요, 그렇지 않습니다       | 교정 방법, 'no_clip', 'l2', 'kld_m0', 'kld_m1', 'kld_m2', 'cdf', 기본값 'no_clip' 지원 |
| samples_count    | int    | 아니요, 그렇지 않습니다       | 샘플 수입니다                                                                              |

#### set_tensor_data()

**기능에 대한 설명입니다**

보정 데이터를 설정합니다

**인터페이스 정의입니다**

```python
set_tensor_data(calib_data)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다   | 형식입니다   | 필요한지 여부 | 설명입니다     |
| ---------- | ------ | -------- | -------- |
| calib_data | 바이트[] | 네       | 데이터를 수정합니다 |

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
# ptq_options
ptq_options = nncase.PTQTensorOptions()
ptq_options.samples_count = cfg.generate_calibs.batch_size
ptq_options.set_tensor_data(np.asarray([sample['data'] for sample in self.calibs]).tobytes())
```

### 4.2.4 컴파일러

**기능에 대한 설명입니다**

신경망 모델을 컴파일하는 Compiler 클래스입니다

**클래스 정의입니다**

```python
py::class_<compiler>(m, "Compiler")
    .def(py::init(&compiler::create))
    .def("import_tflite", &compiler::import_tflite)
    .def("import_onnx", &compiler::import_onnx)
    .def("import_caffe", &compiler::import_caffe)
    .def("compile", &compiler::compile)
    .def("use_ptq", py::overload_cast<ptq_tensor_options>(&compiler::use_ptq))
    .def("gencode", [](compiler &c, std::ostream &stream) { c.gencode(stream); })
    .def("gencode_tobytes", [](compiler &c) {
        std::stringstream ss;
        c.gencode(ss);
        return py::bytes(ss.str());
    })
    .def("create_evaluator", [](compiler &c, uint32_t stage) {
        auto &graph = c.graph(stage);
        return std::make_unique<graph_evaluator>(c.target(), graph);
    });
```

**코드 샘플입니다**

```python
compiler = nncase.Compiler(compile_options)
```

#### import_tflite()

**기능에 대한 설명입니다**

tflite 모델을 가져옵니다

**인터페이스 정의입니다**

```python
import_tflite(model_content, import_options)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다       | 형식입니다          | 필요한지 여부 | 설명입니다           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | 바이트[]        | 네       | 읽은 모델 콘텐츠입니다 |
| import_options | 가져오기 옵션 | 네       | 가져오기 옵션입니다       |

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
model_content = read_model_file(model)
compiler.import_tflite(model_content, import_options)
```

#### import_onnx()

**기능에 대한 설명입니다**

onnx 모델을 가져옵니다

**인터페이스 정의입니다**

```python
import_onnx(model_content, import_options)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다       | 형식입니다          | 필요한지 여부 | 설명입니다           |
| -------------- | ------------- | -------- | -------------- |
| model_content  | 바이트[]        | 네       | 읽은 모델 콘텐츠입니다 |
| import_options | 가져오기 옵션 | 네       | 가져오기 옵션입니다       |

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
model_content = read_model_file(model)
compiler.import_onnx(model_content, import_options)
```

#### import_caffe()

**기능에 대한 설명입니다**

caffe 모델을 가져옵니다

> 사용자는 로컬 컴퓨터에서 cafffe를 직접 컴파일/설치해야 합니다.

**인터페이스 정의입니다**

```python
import_caffe(caffemodel, prototxt)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다   | 형식입니다   | 필요한지 여부 | 설명입니다                 |
| ---------- | ------ | -------- | -------------------- |
| 카페모델 | 바이트[] | 네       | 읽은 caffemodel 내용입니다 |
| 프로토txt   | 바이트[] | 네       | 읽은 prototxt 내용입니다   |

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
# import
caffemodel = read_model_file('test.caffemodel')
prototxt = read_model_file('test.prototxt')
compiler.import_caffe(caffemodel, prototxt)
```

#### use_ptq()

**기능에 대한 설명입니다**

PTQ 구성 옵션을 설정합니다

**인터페이스 정의입니다**

```python
use_ptq(ptq_options)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다    | 형식입니다             | 필요한지 여부 | 설명입니다        |
| ----------- | ---------------- | -------- | ----------- |
| ptq_options | PTQTensorOptions | 네       | PTQ 구성 옵션 |

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
compiler.use_ptq(ptq_options)
```

#### 컴파일 ()

**기능에 대한 설명입니다**

신경망 모델을 컴파일합니다

**인터페이스 정의입니다**

```python
compile()
```

**매개변수를 입력합니다**

해당 없음

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
compiler.compile()
```

#### gencode_tobytes()

**기능에 대한 설명입니다**

코드 바이트 스트림을 생성합니다

**인터페이스 정의입니다**

```python
gencode_tobytes()
```

**매개변수를 입력합니다**

해당 없음

**값을 반환합니다**

바이트[]

**코드 샘플입니다**

```python
kmodel = compiler.gencode_tobytes()
with open(os.path.join(infer_dir, 'test.kmodel'), 'wb') as f:
    f.write(kmodel)
```

## 4.3 모델의 예제를 컴파일합니다

다음 예제에서는 모델 및 파이썬 컴파일 스크립트를 사용합니다

- 모델은 /path/to/nncase_sdk/examples/models/하위 디렉토리에 있습니다
- 파이썬 컴파일 스크립트는 /path/to/nncase_sdk/examples/scripts 하위 디렉토리에 있습니다

### 4.3.1 float32 tflite 모델을 컴파일합니다

- mobilenetv2_tflite_fp32_image.py 스크립트는 다음과 같습니다

```python
import nncase
import os
import argparse

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    # compile_options
    dump_dir = 'tmp/mobilenetv2_tflite_fp32_image'
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    model_content = read_model_file(args.model)
    compiler.import_tflite(model_content, import_options)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- 다음 명령을 실행하여 mobilenetv2의 tflite 모델을 컴파일합니다. target은 k510입니다

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_fp32_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

### 4.3.2 float32 onnx 모델을 컴파일합니다

- onnx 모델의 경우 [nnncase 컴파일을 사용하기 전에](https://github.com/daquexian/onnx-simplifier) ONNX Simplifier를 사용하여 단순화하는 것이 좋습니다
- mobilenetv2_onnx_fp32_image.py 스크립트는 다음과 같습니다

```python
import os
import onnxsim
import onnx
import nncase
import argparse

def parse_model_input_output(model_file):
    onnx_model = onnx.load(model_file)
    input_all = [node.name for node in onnx_model.graph.input]
    input_initializer = [node.name for node in onnx_model.graph.initializer]
    input_names = list(set(input_all) - set(input_initializer))
    input_tensors = [node for node in onnx_model.graph.input if node.name in input_names]

    # input
    inputs= []
    for _, e in enumerate(input_tensors):
        onnx_type = e.type.tensor_type
        input_dict = {}
        input_dict['name'] = e.name
        input_dict['dtype'] = onnx.mapping.TENSOR_TYPE_TO_NP_TYPE[onnx_type.elem_type]
        input_dict['shape'] = [(i.dim_value if i.dim_value != 0 else d) for i, d in zip(
            onnx_type.shape.dim, [1, 3, 224, 224])]
        inputs.append(input_dict)


    return onnx_model, inputs

def onnx_simplify(model_file, dump_dir):
    onnx_model, inputs = parse_model_input_output(model_file)
    onnx_model = onnx.shape_inference.infer_shapes(onnx_model)
    input_shapes = {}
    for input in inputs:
        input_shapes[input['name']] = input['shape']

    onnx_model, check = onnxsim.simplify(onnx_model, input_shapes=input_shapes)
    assert check, "Simplified ONNX model could not be validated"

    model_file = os.path.join(dump_dir, 'simplified.onnx')
    onnx.save_model(onnx_model, model_file)
    return model_file


def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content


def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    dump_dir = 'tmp/mobilenetv2_onnx_fp32_image'
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    # onnx simplify
    model_file = onnx_simplify(args.model, dump_dir)

    # compile_options
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    model_content = read_model_file(model_file)
    compiler.import_onnx(model_content, import_options)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- 다음 명령을 실행하여 mobilenetv2의 onnx 모델을 컴파일하고 target은 k510입니다

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_image.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.3 float32 caffe 모델을 컴파일합니다

- caffe wheel 패키지는[ kendryte caffe에서 ](https://github.com/kendryte/caffe/releases)가져옵니다
- conv2d_caffe_fp32.py 스크립트는 다음과 같습니다

```python
import nncase
import os
import argparse

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--caffemodel", type=str, help='caffemodel file')
    parser.add_argument("--prototxt", type=str, help='prototxt file')
    args = parser.parse_args()

    # compile_options
    dump_dir = 'tmp/conv2d_caffe_fp32'
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    caffemodel = read_model_file(args.caffemodel)
    prototxt = read_model_file(args.prototxt)
    compiler.import_caffe(caffemodel, prototxt)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- 다음 명령을 실행하여 conv2d의 caffe 모델을 컴파일하고 target은 k510입니다

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/conv2d_caffe_fp32.py --target k510 --caffemodel models/test.caffemodel --prototxt models/test.prototxt
```

### 4.3.4 컴파일은 float32 onnx 모델을 추가하기 전에 처리됩니다

- onnx 모델의 경우 [nnncase 컴파일을 사용하기 전에](https://github.com/daquexian/onnx-simplifier) ONNX Simplifier를 사용하여 단순화하는 것이 좋습니다
- mobilenetv2_onnx_fp32_preprocess.py 스크립트는 다음과 같습니다

```python
import os
import onnxsim
import onnx
import nncase
import argparse

def parse_model_input_output(model_file):
    onnx_model = onnx.load(model_file)
    input_all = [node.name for node in onnx_model.graph.input]
    input_initializer = [node.name for node in onnx_model.graph.initializer]
    input_names = list(set(input_all) - set(input_initializer))
    input_tensors = [node for node in onnx_model.graph.input if node.name in input_names]

    # input
    inputs= []
    for _, e in enumerate(input_tensors):
        onnx_type = e.type.tensor_type
        input_dict = {}
        input_dict['name'] = e.name
        input_dict['dtype'] = onnx.mapping.TENSOR_TYPE_TO_NP_TYPE[onnx_type.elem_type]
        input_dict['shape'] = [(i.dim_value if i.dim_value != 0 else d) for i, d in zip(
            onnx_type.shape.dim, [1, 3, 224, 224])]
        inputs.append(input_dict)


    return onnx_model, inputs

def onnx_simplify(model_file, dump_dir):
    onnx_model, inputs = parse_model_input_output(model_file)
    onnx_model = onnx.shape_inference.infer_shapes(onnx_model)
    input_shapes = {}
    for input in inputs:
        input_shapes[input['name']] = input['shape']

    onnx_model, check = onnxsim.simplify(onnx_model, input_shapes=input_shapes)
    assert check, "Simplified ONNX model could not be validated"

    model_file = os.path.join(dump_dir, 'simplified.onnx')
    onnx.save_model(onnx_model, model_file)
    return model_file


def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content


def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    dump_dir = 'tmp/mobilenetv2_onnx_fp32_preprocess'
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    # onnx simplify
    model_file = onnx_simplify(args.model, dump_dir)

    # compile_options
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.input_type = 'uint8'
    compile_options.preprocess = True
    compile_options.swapRB = True
    compile_options.input_layout = 'NHWC'
    compile_options.output_layout = 'NCHW'
    compile_options.input_shape = [1, 256, 256, 3]
    compile_options.mean = [0.485, 0.456, 0.406]
    compile_options.std = [0.229, 0.224, 0.225]
    compile_options.input_range = [0, 1]
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # import
    model_content = read_model_file(model_file)
    compiler.import_onnx(model_content, import_options)

    # compile
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- 다음 명령을 실행하여 추가 전처리된 mobilenetv2의 onnx 모델을 컴파일할 수 있으며 target은 k510입니다

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_fp32_preprocess.py --target k510 --model models/mobilenetv2-7.onnx
```

### 4.3.5 uint8 양자화 tflite 모델을 컴파일합니다

- mobilenetv2_tflite_uint8_image.py 스크립트는 다음과 같습니다

```python
import nncase
import os
import argparse
import numpy as np

def read_model_file(model_file):
    with open(model_file, 'rb') as f:
        model_content = f.read()
    return model_content

def generate_data(shape, batch):
    shape[0] *= batch
    data = np.random.rand(*shape).astype(np.float32)
    return data

def main():
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--target", type=str, help='target to run')
    parser.add_argument("--model", type=str, help='model file')
    args = parser.parse_args()

    input_shape = [1, 224, 224, 3]

    # compile_options
    dump_dir = 'tmp/mobilenetv2_tflite_uint8_image'
    compile_options = nncase.CompileOptions()
    compile_options.target = args.target
    compile_options.input_type = 'float32'
    compile_options.input_layout = 'NHWC'
    compile_options.output_layout = 'NHWC'
    compile_options.dump_ir = True
    compile_options.dump_asm = True
    compile_options.dump_dir = dump_dir

    # compiler
    compiler = nncase.Compiler(compile_options)

    # import_options
    import_options = nncase.ImportOptions()

    # quantize model
    compile_options.quant_type = 'uint8'

    # ptq_options
    ptq_options = nncase.PTQTensorOptions()
    ptq_options.samples_count = 10
    ptq_options.set_tensor_data(generate_data(input_shape, ptq_options.samples_count).tobytes())

    # import
    model_content = read_model_file(args.model)
    compiler.import_tflite(model_content, import_options)

    # compile
    compiler.use_ptq(ptq_options)
    compiler.compile()

    # kmodel
    kmodel = compiler.gencode_tobytes()
    with open(os.path.join(dump_dir, 'test.kmodel'), 'wb') as f:
        f.write(kmodel)

if __name__ == '__main__':
    main()
```

- 다음 명령을 실행하여 uint8 양자화된 mobilenetv2의 tflite 모델을 컴파일하고 target은 k510입니다

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_tflite_uint8_image.py --target k510 --model models/mobilenet_v2_1.0_224.tflite
```

## 4.4 추론 모델 API

모델 API를 컴파일하는 것 외에도 nncase는 추론 모델의 API를 제공하고, PC에서 추론하기 전에 생성된 kmodel을 컴파일하고, nncase 추론 결과가 해당 딥 러닝 프레임워크의 runtime 결과와 일치하는지 확인하는 등의 기능을 제공합니다.

### 4.4.1 메모리 범위

**기능에 대한 설명입니다**

메모리 범위를 나타내는 MemoryRange 클래스입니다

**클래스 정의입니다**

```python
py::class_<memory_range>(m, "MemoryRange")
    .def_readwrite("location", &memory_range::memory_location)
    .def_property(
        "dtype", [](const memory_range &range) { return to_dtype(range.datatype); },
        [](memory_range &range, py::object dtype) { range.datatype = from_dtype(py::dtype::from_args(dtype)); })
    .def_readwrite("start", &memory_range::start)
    .def_readwrite("size", &memory_range::size);
```

각 속성은 아래에 설명되어 있습니다

| 속성 이름입니다 | 형식입니다           | 필요한지 여부 | 설명입니다                                                                       |
| -------- | -------------- | -------- | -------------------------------------------------------------------------- |
| 위치 | int            | 아니요, 그렇지 않습니다       | 메모리 위치, 0은 input, 1은 output, 2는 rdata, 3은 data, 4는 shared_data |
| dtype    | 파이썬 데이터 형식입니다 | 아니요, 그렇지 않습니다       | 데이터 형식입니다                                                                   |
| 시작하다    | int            | 아니요, 그렇지 않습니다       | 메모리 시작 주소입니다                                                               |
| 크기     | int            | 아니요, 그렇지 않습니다       | 메모리 크기입니다                                                                   |

**코드 샘플입니다**

MemoryRange를 인스턴스화합니다

```python
mr = nncase.MemoryRange()
```

### 4.4.2 런타임 텐서

**기능에 대한 설명입니다**

런타임 tensor를 나타내는 RuntimeTensor 클래스입니다

**클래스 정의입니다**

```python
py::class_<runtime_tensor>(m, "RuntimeTensor")
    .def_static("from_numpy", [](py::array arr) {
        auto src_buffer = arr.request();
        auto datatype = from_dtype(arr.dtype());
        auto tensor = host_runtime_tensor::create(
            datatype,
            to_rt_shape(src_buffer.shape),
            to_rt_strides(src_buffer.itemsize, src_buffer.strides),
            gsl::make_span(reinterpret_cast<gsl::byte *>(src_buffer.ptr), src_buffer.size * src_buffer.itemsize),
            [=](gsl::byte *) { arr.dec_ref(); })
                          .unwrap_or_throw();
        arr.inc_ref();
        return tensor;
    })
    .def("copy_to", [](runtime_tensor &from, runtime_tensor &to) {
        from.copy_to(to).unwrap_or_throw();
    })
    .def("to_numpy", [](runtime_tensor &tensor) {
        auto host = tensor.as_host().unwrap_or_throw();
        auto src_map = std::move(hrt::map(host, hrt::map_read).unwrap_or_throw());
        auto src_buffer = src_map.buffer();
        return py::array(
            to_dtype(tensor.datatype()),
            tensor.shape(),
            to_py_strides(runtime::get_bytes(tensor.datatype()), tensor.strides()),
            src_buffer.data());
    })
    .def_property_readonly("dtype", [](runtime_tensor &tensor) {
        return to_dtype(tensor.datatype());
    })
    .def_property_readonly("shape", [](runtime_tensor &tensor) {
        return to_py_shape(tensor.shape());
    });
```

각 속성은 아래에 설명되어 있습니다

| 속성 이름입니다 | 형식입니다 | 필요한지 여부 | 설명입니다             |
| -------- | ---- | -------- | ---------------- |
| dtype    | int  | 아니요, 그렇지 않습니다       | tensor의 데이터 형식입니다 |
| 모양    | 목록 | 아니요, 그렇지 않습니다       | tensor의 모양입니다     |

#### from_numpy()

**기능에 대한 설명입니다**

numpy.ndarray에서 RuntimeTensor 객체를 생성합니다

**인터페이스 정의입니다**

```python
from_numpy(py::array arr)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다          | 필요한지 여부 | 설명입니다              |
| -------- | ------------- | -------- | ----------------- |
| 도착      | numpy.ndarray | 네       | numpy.ndarray 객체입니다 |

**값을 반환합니다**

런타임텐서

**코드 샘플입니다**

```python
tensor = nncase.RuntimeTensor.from_numpy(self.inputs[i]['data'])
```

#### copy_to()

**기능에 대한 설명입니다**

RuntimeTensor를 복사합니다

**인터페이스 정의입니다**

```python
copy_to(RuntimeTensor to)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다          | 필요한지 여부 | 설명입니다              |
| -------- | ------------- | -------- | ----------------- |
| 받는 사람       | 런타임텐서 | 네       | RuntimeTensor 객체입니다 |

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
sim.get_output_tensor(i).copy_to(to)
```

#### to_numpy()

**기능에 대한 설명입니다**

RuntimeTensor를 numpy.ndarray 객체로 변환합니다

**인터페이스 정의입니다**

```python
to_numpy()
```

**매개변수를 입력합니다**

해당 없음

**값을 반환합니다**

numpy.ndarray 객체입니다

**코드 샘플입니다**

```python
arr = sim.get_output_tensor(i).to_numpy()
```

### 4.4.3 시뮬레이터

**기능에 대한 설명입니다**

Simulator 클래스, PC에서 kmodel을 추론하는 데 사용됩니다

**클래스 정의입니다**

```python
py::class_<interpreter>(m, "Simulator")
    .def(py::init())
    .def("load_model", [](interpreter &interp, gsl::span<const gsl::byte> buffer) { interp.load_model(buffer).unwrap_or_throw(); })
    .def_property_readonly("inputs_size", &interpreter::inputs_size)
    .def_property_readonly("outputs_size", &interpreter::outputs_size)
    .def("get_input_desc", &interpreter::input_desc)
    .def("get_output_desc", &interpreter::output_desc)
    .def("get_input_tensor", [](interpreter &interp, size_t index) { return interp.input_tensor(index).unwrap_or_throw(); })
    .def("set_input_tensor", [](interpreter &interp, size_t index, runtime_tensor tensor) { return interp.input_tensor(index, tensor).unwrap_or_throw(); })
    .def("get_output_tensor", [](interpreter &interp, size_t index) { return interp.output_tensor(index).unwrap_or_throw(); })
    .def("set_output_tensor", [](interpreter &interp, size_t index, runtime_tensor tensor) { return interp.output_tensor(index, tensor).unwrap_or_throw(); })
    .def("run", [](interpreter &interp) { interp.run().unwrap_or_throw(); });
```

각 속성은 아래에 설명되어 있습니다

| 속성 이름입니다     | 형식입니다 | 필요한지 여부 | 설명입니다     |
| ------------ | ---- | -------- | -------- |
| inputs_size  | int  | 아니요, 그렇지 않습니다       | 숫자를 입력합니다 |
| outputs_size | int  | 아니요, 그렇지 않습니다       | 출력 수입니다 |

**코드 샘플입니다**

Simulator를 인스턴스화합니다

```python
sim = nncase.Simulator()
```

#### load_model()

**기능에 대한 설명입니다**

kmodel을 로드합니다

**인터페이스 정의입니다**

```python
load_model(model_content)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다      | 형식입니다   | 필요한지 여부 | 설명입니다         |
| ------------- | ------ | -------- | ------------ |
| model_content | 바이트[] | 네       | kmodel 바이트 스트림입니다 |

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
sim.load_model(kmodel)
```

#### get_input_desc()

**기능에 대한 설명입니다**

지정된 인덱스의 입력에 대한 설명 정보를 가져옵니다

**인터페이스 정의입니다**

```python
get_input_desc(index)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다 | 필요한지 여부 | 설명입니다       |
| -------- | ---- | -------- | ---------- |
| 색인    | int  | 네       | 입력한 인덱스입니다 |

**값을 반환합니다**

메모리 범위

**코드 샘플입니다**

```python
input_desc_0 = sim.get_input_desc(0)
```

#### get_output_desc()

**기능에 대한 설명입니다**

지정된 인덱스의 출력에 대한 설명 정보를 가져옵니다

**인터페이스 정의입니다**

```python
get_output_desc(index)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다 | 필요한지 여부 | 설명입니다       |
| -------- | ---- | -------- | ---------- |
| 색인    | int  | 네       | 출력의 인덱스입니다 |

**값을 반환합니다**

메모리 범위

**코드 샘플입니다**

```python
output_desc_0 = sim.get_output_desc(0)
```

#### get_input_tensor()

**기능에 대한 설명입니다**

지정된 인덱스에 대한 입력에 대한 RuntimeTensor를 가져옵니다

**인터페이스 정의입니다**

```python
get_input_tensor(index)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다 | 필요한지 여부 | 설명입니다             |
| -------- | ---- | -------- | ---------------- |
| 색인    | int  | 네       | tensor의 인덱스를 입력합니다 |

**값을 반환합니다**

런타임텐서

**코드 샘플입니다**

```python
input_tensor_0 = sim.get_input_tensor(0)
```

#### set_input_tensor()

**기능에 대한 설명입니다**

지정된 인덱스에 대한 입력에 대한 RuntimeTensor를 설정합니다

**인터페이스 정의입니다**

```python
set_input_tensor(index, tensor)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다          | 필요한지 여부 | 설명입니다                    |
| -------- | ------------- | -------- | ----------------------- |
| 색인    | int           | 네       | RuntimeTensor의 인덱스를 입력합니다 |
| 텐서   | 런타임텐서 | 네       | RuntimeTensor를 입력합니다       |

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(self.inputs[0]['data']))
```

#### get_output_tensor()

**기능에 대한 설명입니다**

지정된 인덱스의 출력에 대한 RuntimeTensor를 가져옵니다

**인터페이스 정의입니다**

```python
get_output_tensor(index)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다 | 필요한지 여부 | 설명입니다                    |
| -------- | ---- | -------- | ----------------------- |
| 색인    | int  | 네       | RuntimeTensor의 인덱스를 출력합니다 |

**값을 반환합니다**

런타임텐서

**코드 샘플입니다**

```python
output_arr_0 = sim.get_output_tensor(0).to_numpy()
```

#### set_output_tensor()

**기능에 대한 설명입니다**

지정된 인덱스의 출력에 대한 RuntimeTensor를 설정합니다

**인터페이스 정의입니다**

```python
set_output_tensor(index, tensor)
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다          | 필요한지 여부 | 설명입니다                    |
| -------- | ------------- | -------- | ----------------------- |
| 색인    | int           | 네       | RuntimeTensor의 인덱스를 출력합니다 |
| 텐서   | 런타임텐서 | 네       | RuntimeTensor를 출력합니다       |

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
sim.set_output_tensor(0, tensor)
```

#### 실행 ()

**기능에 대한 설명입니다**

kmodel 추리를 실행하다

**인터페이스 정의입니다**

```python
run()
```

**매개변수를 입력합니다**

해당 없음

**값을 반환합니다**

해당 없음

**코드 샘플입니다**

```python
sim.run()
```

## 4.5 추론 모델의 예입니다

**사전 조건**: mobilenetv2_onnx_fp32_image.py 스크립트가 mobilenetv2-7.onnx 모델로 컴파일되었습니다

mobilenetv2_onnx_simu.py /path/to/nncase_sdk/examples/scripts 하위 디렉토리에 있습니다

```python
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
    parser = argparse.ArgumentParser(prog="nncase")
    parser.add_argument("--model_file", type=str, help='original model file')
    parser.add_argument("--kmodel_file", type=str, help='kmodel file')
    parser.add_argument("--input_file", type=str, help='input bin file for kmodel')
    args = parser.parse_args()

    # create simulator
    sim = nncase.Simulator()

    # read kmodel
    kmodel = read_model_file(args.kmodel_file)

    # load kmodel
    sim.load_model(kmodel)

    # read input.bin
    input_tensor=sim.get_input_tensor(0).to_numpy()
    input = np.fromfile(args.input_file, input_tensor.dtype).reshape(input_tensor.shape)

    # set input for simulator
    sim.set_input_tensor(0, nncase.RuntimeTensor.from_numpy(input))

    # simulator inference
    nncase_results = []
    sim.run()
    for i in range(sim.outputs_size):
        nncase_result = sim.get_output_tensor(i).to_numpy()
        nncase_results.append(copy.deepcopy(nncase_result))

    # cpu inference
    cpu_results = []
    ort_session = ort.InferenceSession(args.model_file)
    input_name = ort_session.get_inputs()[0].name
    output_name = ort_session.get_outputs()[0].name
    cpu_results = ort_session.run([output_name], { input_name : input })

    # compare
    for i in range(sim.outputs_size):
        cos = cosine(np.reshape(nncase_results[i], (-1)), np.reshape(cpu_results[i], (-1)))
        print('output {0} cosine similarity : {1}'.format(i, cos))

if __name__ == '__main__':
    main()
```

추론 스크립트를 실행합니다

```shell
cd /path/to/nncase_sdk/examples
python3 scripts/mobilenetv2_onnx_simu.py --model_file models/mobilenetv2-7.onnx --kmodel_file tmp/mobilenetv2_onnx_fp32_image/test.kmodel --input_file mobilenetv2_onnx_fp32_image/data/input_0_0.bin
```

nncase simulator와 cpu 추론 결과는 다음과 같습니다

```shell
... ...
output 0 cosine similarity : 0.9992437958717346
```

# 5 nncase 런타임 라이브러리입니다

## 5.1 nncase Runtime 소개

nncase runtime은 AI 장치에 kmodel / 입력 데이터 설정 / KPU 계산 수행 / 출력 데이터 가져오기 등에 사용됩니다.

현재 nncase sdk/riscv64 디렉토리에서 관련 헤더 파일 및 정적 라이브러리와 함께 C**++ 버전의 API**만 사용할 수 있습니다

```bash
$ tree -L 3 riscv64/
riscv64/
├── include
│   ├── gsl
│   │   └── gsl-lite.hpp
│   ├── gsl-lite
│   │   └── gsl-lite.hpp
│   ├── mpark
│   │   ├── config.hpp
│   │   ├── in_place.hpp
│   │   ├── lib.hpp
│   │   └── variant.hpp
│   └── nncase
│       ├── functional
│       ├── kernels
│       ├── runtime
│       └── version.h
└── lib
    ├── cmake
    │   ├── nncasefunctional
    │   ├── nncase_rt_modules_k510
    │   └── nncaseruntime
    ├── libnncase.functional.a
    ├── libnncase.rt_modules.k510.a
    └── libnncase.runtime.a

13 directories, 10 files
```

## 5.2 런타임 API

### 5.2.1 클래스 runtime_tensor

모델 입력/출력 데이터를 저장하는 데 사용되는 tensor입니다

#### hrt::만들기()

**기능에 대한 설명입니다**

runtime_tensor 만듭니다

**인터페이스 정의입니다**

```C++
(1) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;

(2) NNCASE_API result<runtime_tensor> create(datatype_t datatype, runtime_shape_t shape, gsl::span<gsl::byte> data, bool copy, memory_pool_t pool = pool_cpu_only, uintptr_t physical_address = 0) noexcept;
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다         | 형식입니다                  | 필요한지 여부 | 설명입니다                              |
| ---------------- | --------------------- | -------- | --------------------------------- |
| 데이터 유형         | datatype_t            | 네       | dt_float32 같은 데이터 형식입니다            |
| 모양            | runtime_shape_t       | 네       | tensor의 모양입니다                      |
| 데이터             | gsl::span\<gsl::byte> | 네       | 사용자 상태 데이터 버퍼입니다                  |
| 복사             | 부울                  | 네       | 복사할지 여부입니다                          |
| 풀             | memory_pool_t         | 아니요, 그렇지 않습니다       | 메모리 풀 유형, 기본값은 pool_cpu_only |
| physical_address | uintptr_t             | 아니요, 그렇지 않습니다       | 실제 주소, 기본값은 0입니다               |

**값을 반환합니다**

결과<runtime_tensor>

코드 샘플입니다

```c++
// create input
auto in_shape = interp.input_shape(0);
auto input_tensor = host_runtime_tensor::create(dt_float32, in_shape,
                                                {(gsl::byte *)mat.data, mat.cols * mat.rows * mat.elemSize()},
                                                true, hrt::pool_shared).expect("cannot create input tensor");
```

### 5.2.2 클래스 인터프리터

interpreter는 load_model()/run()/input_tensor()/output_tensor()와 같은 핵심 기능 함수를 제공하는 nncase runtime의 실행 인스턴스입니다.

#### load_model()

**기능에 대한 설명입니다**

kmodel 모델을 로드합니다

**인터페이스 정의입니다**

```C++
 NNCASE_NODISCARD result<void> load_model(gsl::span<const gsl::byte> buffer) noexcept;
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다                            | 필요한지 여부 | 설명입니다          |
| -------- | ------------------------------- | -------- | ------------- |
| 완충기   | gsl::span `<const gsl::byte>` | 네       | kmodel 버퍼 |

**값을 반환합니다**

결과 `<void>`

**코드 샘플입니다**

```c++
template <class T>
std::vector<T>read_binary_file(const char *file_name)
{
  std::ifstream ifs(file_name, std::ios::binary);
  ifs.seekg(0, ifs.end);
  size_t len = ifs.tellg();
  std::vector<T> vec(len / sizeof(T), 0);
  ifs.seekg(0, ifs.beg);
  ifs.read(reinterpret_cast<char*>(vec.data()), len);
  ifs.close();
  return vec;
}

interpreter interp;
auto model = read_binary_file<unsigned char>(kmodel);
interp.load_model({(const gsl::byte *)model.data(), model.size()}).expect("cannot load model.");
```

#### inputs_size()

**기능에 대한 설명입니다**

모델 입력 수를 가져옵니다

**인터페이스 정의입니다**

```C++
size_t inputs_size() const noexcept;
```

**매개변수를 입력합니다**

해당 없음

**값을 반환합니다**

size_t

**코드 샘플입니다**

```c++
auto inputs_size = interp.inputs_size();
```

#### outputs_size()

**기능에 대한 설명입니다**

모델 출력 수를 가져옵니다

**인터페이스 정의입니다**

```C++
size_t outputs_size() const noexcept;
```

**매개변수를 입력합니다**

해당 없음

**값을 반환합니다**

size_t

**코드 샘플입니다**

```c++
auto outputs_size = interp.outputs_size();
```

#### input_shape()

**기능에 대한 설명입니다**

모델 지정 입력의 셰이프를 가져옵니다

**인터페이스 정의입니다**

```C++
const runtime_shape_t &input_shape(size_t index) const noexcept;
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다   | 필요한지 여부 | 설명입니다       |
| -------- | ------ | -------- | ---------- |
| 색인    | size_t | 네       | 입력한 인덱스입니다 |

**값을 반환합니다**

runtime_shape_t

**코드 샘플입니다**

```c++
auto in_shape = interp.input_shape(0);
```

#### output_shape()

**기능에 대한 설명입니다**

모델에서 지정한 출력의 셰이프를 가져옵니다

**인터페이스 정의입니다**

```C++
const runtime_shape_t &output_shape(size_t index) const noexcept;
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다   | 필요한지 여부 | 설명입니다       |
| -------- | ------ | -------- | ---------- |
| 색인    | size_t | 네       | 출력의 인덱스입니다 |

**값을 반환합니다**

runtime_shape_t

**코드 샘플입니다**

```c++
auto out_shape = interp.output_shape(0);
```

#### input_tensor()

**기능에 대한 설명입니다**

지정된 인덱스의 input tensor를 가져오거나 설정합니다

**인터페이스 정의입니다**

```C++
(1) result<runtime_tensor> input_tensor(size_t index) noexcept;
(2) result<void> input_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다           | 필요한지 여부 | 설명입니다                     |
| -------- | -------------- | -------- | ------------------------ |
| 색인    | size_t         | 네       | kmodel 버퍼            |
| 텐서   | runtime_tensor | 네       | 해당 runtime tensor를 입력합니다 |

**값을 반환합니다**

(1) result를 반환합니다<runtime_tensor>

(2) result를 반환합니다 `<void>`

**코드 샘플입니다**

```c++
// set input
interp.input_tensor(0, input_tensor).expect("cannot set input tensor");
```

#### output_tensor()

**기능에 대한 설명입니다**

지정된 인덱스의 output tensor를 가져오거나 설정합니다

**인터페이스 정의입니다**

```C++
(1) result<runtime_tensor> output_tensor(size_t index) noexcept;
(2) result<void> output_tensor(size_t index, runtime_tensor tensor) noexcept;
```

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다           | 필요한지 여부 | 설명입니다                     |
| -------- | -------------- | -------- | ------------------------ |
| 색인    | size_t         | 네       |                          |
| 텐서   | runtime_tensor | 네       | 해당 runtime tensor를 입력합니다 |

**값을 반환합니다**

(1) result를 반환합니다<runtime_tensor>

(2) result를 반환합니다 `<void>`

**코드 샘플입니다**

```c++
// get output
auto output_tensor = interp.output_tensor(0).expect("cannot get output tensor");
auto mapped_buf = std::move(hrt::map(output_tensor, hrt::map_read).unwrap_or_throw());
float *output_data = reinterpret_cast<float *>(mapped_buf.buffer().data());
auto out_shape = interp.output_shape(0);
auto it = std::max_element(output_data, output_data + compute_size(out_shape));
size_t idx = it - output_data;
std::cout << "image classification result: " << labels[idx] << "(" << *it << ")" << std::endl;
```

#### 실행 ()

**기능에 대한 설명입니다**

kpu 계산을 수행합니다

**인터페이스 정의입니다**

```C++
result<void> run() noexcept;
```

**매개변수를 입력합니다**

해당 없음

**값을 반환합니다**

결과 `<void>`

**코드 샘플입니다**

```c++
// run
interp.run().expect("error occurred in running model");
```

## 5.3 Runtime 예제입니다

샘플 코드는 /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image 있습니다

**접두사 조건**

- mobilenetv2_onnx_fp32_image.py 스크립트가 mobilenetv2-7.onnx 모델로 컴파일되었습니다
- 이 예제는 OpenCV 라이브러리에 의존하므로 예제의 CMakeLists .txt OpenCV의 경로를 지정해야 합니다.

**앱을 교차 컴파일합니다**

```shell
cd /path/to/nncase_sdk/examples
./build.sh
```

마지막으로 out/bin 디렉터리에서 mobilenetv2_onnx_fp32_image 생성됩니다

**k510 EVB 보드가 실행됩니다**

다음 파일을 k510 EVB 보드에 복사합니다

| 파일입니다                        | 참고 사항                                                         |
| --------------------------- | ------------------------------------------------------------ |
| mobilenetv2_onnx_fp32_image | examples 빌드를 교차 컴파일합니다                                         |
| test.kmodel                 | mobilenetv2_onnx_fp32_image.py 사용하여 mobilenetv2-7.onnx 빌드를 컴파일합니다 |
| cat.png 및 labels_1000.txt    | /path/to/nncase_sdk/examples/mobilenetv2_onnx_fp32_image/data/하위 디렉토리에 있습니다 |

```bash
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mnt/zhangyang/nncase_check/lib/gomp:/mnt/zhangyang/nncase_check/lib/opencv
$ ./mobilenetv2_onnx_fp32_image test.kmodel cat.png labels_1000.txt
case ./mobilenetv2_onnx_fp32_image build at Mar  1 2022 16:31:29
interp.run() duration: 12.6642 ms
image classification result: tiger cat(9.25)
```

# 6 함수형 프로그래밍 라이브러리(런타임 지원)

## 6.1 Functional 소개

nncase Functional은 사용자가 모델을 앞뒤로 처리할 때 사용 편의성을 향상시키는 데 사용됩니다

현재 nncase sdk의 riscv64 디렉토리에서 관련 헤더 파일 및 라이브러리인 API의 C++ 버전만 사용할 수 있습니다.

## 6.2 아피스

### 6.2.1 정사각형

**기능에 대한 설명입니다**

제곱을 계산, 현재 입력 uint8/int8을 지원, 출력은 uint8 / int8, 입력이 고정 소수점이고 출력이 부동 소수점 인 경우 양자화 매개 변수를 설정해야합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`square`](#ops_8h_1adff2f60c7c045a9840519eab2c04d127)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 샘플입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto squared = F::square(input, output_type).unwrap_or_throw();
```

### 6.2.2 스퀘어

**기능에 대한 설명입니다**

루트 번호 값을 계산, 현재 uint8/int8의 입력을 지원, 출력은 uint8/int8, 입력이 고정 소수점이며 출력이 부동 소수점 인 경우 양자화 매개 변수를 설정해야합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sqrt`](#ops_8h_1a53f8dde3dd4e27058b5dc743eb5dd076)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 샘플입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sqrt(input, output_type).unwrap_or_throw();
```

### 6.2.3 로그

**기능에 대한 설명입니다**

로그 값을 계산하면 입력의 음수가 Nan으로 변환되고 현재 uint8/int8 입력이 지원되며 출력은 uint8/int8이며 입력이 고정 소수점이고 출력이 부동 소수점인 경우 양자화 매개 변수를 설정해야 합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`log`](#ops_8h_1a91df53276c3f1511427d4ac1a0140b71)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 샘플입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::log(input, output_type).unwrap_or_throw();
```

### 6.2.4 특급

**기능에 대한 설명입니다**

exp 값을 계산하면 현재 uint8/int8 입력이 지원되고 출력은 uint8/int8이며 입력이 고정 소수점이고 출력이 부동 소수점인 경우 양자화 매개 변수를 설정해야 합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`exp`](#ops_8h_1a2c6ce457805a5ba515fa7454fb4aede0)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 샘플입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::exp(input, output_type).unwrap_or_throw();
```

### 6.2.5 없이

**기능에 대한 설명입니다**

sin 값을 계산하면 현재 uint8/int8 입력이 지원되고 출력은 uint8/int8이며 입력이 고정 소수점이고 출력이 부동 소수점인 경우 양자화 매개 변수를 설정해야 합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`sin`](#ops_8h_1a9605b2b0dc9a6892ce878bda14586890)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::sin(input, output_type).unwrap_or_throw();
```

### 6.2.6 본체

**기능에 대한 설명입니다**

cos 값을 계산하면 현재 uint8/int8 입력이 지원되고 출력은 uint8/int8이며 입력이 고정 소수점이고 출력이 부동 소수점인 경우 양자화 매개 변수를 설정해야 합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`cos`](#ops_8h_1a71d36c13c82f4c411f24d030cf333249)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::cos(input, output_type).unwrap_or_throw();
```

### 6.2.7 라운드

**기능에 대한 설명입니다**

round 값을 계산하고 현재 uint8/int8 입력을 지원하며 출력은 uint8/int8이며 입력이 고정 소수점이고 출력이 부동 소수점인 경우 양자화 매개 변수를 설정해야 합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`round`](#ops_8h_1a81db8ac4866004f75fb65db876262785)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::round(input, output_type).unwrap_or_throw();
```

### 6.2.8층

**기능에 대한 설명입니다**

floor 값을 계산하면 현재 uint8/int8 입력이 지원되고 출력은 uint8/int8이며 입력이 고정 소수점이고 출력이 부동 소수점인 경우 양자화 매개 변수를 설정해야 합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`floor`](#ops_8h_1a1079af8fe9fb6edbb2906d91fac12635)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::floor(input, output_type).unwrap_or_throw();
```

### 6.2.9 세일

**기능에 대한 설명입니다**

ceil 값을 계산하면 현재 uint8/int8 입력이 지원되고 출력은 uint8/int8이므로 입력이 고정 소수점이고 출력이 부동 소수점인 경우 양자화 매개 변수를 설정해야 합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`ceil`](#ops_8h_1ad3b78c97f1e5348a26de7e5ba2396fb7)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::ceil(input, output_type).unwrap_or_throw();
```

### 6.2.10 복근

**기능에 대한 설명입니다**

abs 값을 계산하면 현재 uint8/int8 입력이 지원되고 출력은 uint8/int8이며 입력이 고정 소수점이고 출력이 부동 소수점인 경우 양자화 매개 변수를 설정해야 합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`abs`](#ops_8h_1ad8290dc793bae0dc22b3baf9e0f80c14)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::abs(input, output_type).unwrap_or_throw();
```

### 6.2.11 부정

**기능에 대한 설명입니다**

neg 값을 계산하면 현재 uint8/int8 입력이 지원되고 출력은 uint8/int8이며 입력이 고정 소수점이고 출력이 부동 소수점인 경우 양자화 매개 변수를 설정해야 합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`neg`](#ops_8h_1aa1b7858802e1afce78db72163c5210d8)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
if ((input_type == dt_uint8 or input_type == dt_int8) and (output_type == dt_float32 or output_type == dt_bfloat16))
{
    input.quant_param(xxx);
}
auto output = F::neg(input, output_type).unwrap_or_throw();
```

### 6.2.12 양자화

**기능에 대한 설명입니다**

입력 dt_bfloat16, dt_float32 데이터, 출력 dt_int8 또는 dt_uint8 출력입니다

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`quantize`](#ops_8h_1ad8ad779083b5c08da520d2f1c2469c3a)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                                |
| --------- | -------------- | -------- | ----------------------------------- |
| `input` | runtime_tensor | 네       | 입력, 유형은 float32 또는 bfloat16이어야 합니다 |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다                 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
auto quantized = F::quantize(input, dt_int8).unwrap_or_throw();
```

### 6.2.13 양자화

**기능에 대한 설명입니다**

uint8 or int8 입력을 입력하여 float or bfloat 데이터로 변환합니다. 사용자는 데이터를 미리 정량화하기 위해 올바른 양자화 매개 변수를 설정해야 합니다.

**인터페이스 정의입니다**

`public inline NNCASE_API`[`result`](#classnncase_1_1result)`< runtime::runtime_tensor >`[`dequantize`](#ops_8h_1ab91a262349baf393c91abad6f393de24)`(runtime::runtime_tensor & input,datatype_t dtype) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다  | 형식입니다           | 필요한지 여부 | 설명입니다                |
| --------- | -------------- | -------- | ------------------- |
| `input` | runtime_tensor | 네       | 입력합니다                |
| `dtype` | datatype_t     | 네       | tensor datatype을 출력합니다 |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
input.quant_param({ 0, 1 });
auto dequantized = F::dequantize(input, output_type).unwrap_or_throw();
```

### 6.2.14 자르기

**기능에 대한 설명입니다**

주어진 bboxs, 원래 tensor에서 자르기 및 resize는 새로운 tensor로 출력됩니다. dt_bfloat16, dt_float32, dt_int8, dt_uint8 형식 출력을 수락하고 동일한 형식을 출력합니다.

**인터페이스 정의입니다**

`NNCASE_API inline result<runtime::runtime_tensor> crop(runtime::runtime_tensor &input, runtime::runtime_tensor &bbox, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다           | 형식입니다                | 필요한지 여부 | 설명입니다                                                                                     |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------------- |
| 입력              | runtime_tensor      | 네       | 데이터를 입력하려면 형식 배열이 필요하며 [n, c, h, w] , 데이터가 uint8 또는 int8인 경우 데이터 양자화 매개 변수의 정확성을 보장합니다       |
| 증권 시세 표시기               | runtime_tensor      | 네       | bbox 데이터를 입력하려면 [1,1,m,4] 형식 배열이 필요하며 내부 데이터는 형식[y0, x0, y1, x1]입니다[플로트32,bfloat16] |
| out_h              | size_t              | 네       | 출력 데이터 height                                                                           |
| out_w              | size_t              | 네       | 데이터 위드를 입력합니다                                                                            |
| resize_mode        | image_resize_mode_t | 네       | resize 메서드 패턴입니다                                                                           |
| align_corners      | 부울                | 네       | resize가 align_corners                                                    |
| half_pixel_centers | 부울                | 네       | resize가 픽셀 중심 정렬 여부를 확인합니다                                                                  |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
auto bbox = get_rand_bbox(input_shape, roi_amount);
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::crop(input, bbox, out_h, out_w, resize_mode).unwrap_or_throw();
```

### 6.2.15 크기 조정

**기능에 대한 설명입니다**

출력 높이 너비를 감안할 때 입력 tensor resize를 새 크기로 가져옵니다. dt_bfloat16, dt_float32, dt_int8, dt_uint8 형식 출력을 수락하고 동일한 형식을 출력합니다.

**인터페이스 정의입니다**

`NNCASE_API inline result<runtime::runtime_tensor> resize(runtime::runtime_tensor &input, size_t out_h, size_t out_w, image_resize_mode_t resize_mode, bool align_corners, bool half_pixel_centers) noexcept`

**매개변수를 입력합니다**

| 매개 변수 이름입니다           | 형식입니다                | 필요한지 여부 | 설명입니다                                                                               |
| ------------------ | ------------------- | -------- | ---------------------------------------------------------------------------------- |
| 입력              | runtime_tensor      | 네       | 데이터를 입력하려면 형식 배열이 필요하며 [n, c, h, w] 데이터가 uint8 또는 int8인 경우 데이터 양자화 매개 변수의 정확성을 보장합니다 |
| out_h              | size_t              | 네       | 출력 데이터 height                                                                     |
| out_w              | size_t              | 네       | 데이터 위드를 입력합니다                                                                      |
| resize_mode        | image_resize_mode_t | 네       | resize 메서드 패턴입니다                                                                     |
| align_corners      | 부울                | 네       | resize가 align_corners                                              |
| half_pixel_centers | 부울                | 네       | resize가 픽셀 중심 정렬 여부를 확인합니다                                                            |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
auto &&[out_h, out_w] = get_rand_out_hw();
auto output_opt = F::resize(input, out_h, out_w, resize_mode, false, false).unwrap_or_throw();
```

### 6.2.16 패드

**기능에 대한 설명입니다**

각 차원에서 padding 데이터는 dt_bfloat16, dt_float32, dt_int8, dt_uint8 형식 출력을 수락하고 동일한 형식을 출력합니다.

**인터페이스 정의입니다**

`NNCASE_API inline result<runtime::runtime_tensor> pad(runtime::runtime_tensor &input, runtime_paddings_t &paddings, pad_mode_t pad_mode, float fill_v)`

**매개변수를 입력합니다**

| 매개 변수 이름입니다 | 형식입니다               | 필요한지 여부 | 설명입니다                                                                                                                                       |
| -------- | ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 입력    | runtime_tensor     | 네       | 데이터를 입력하거나 uint8 또는 int8인 경우 데이터 양자화 매개 변수의 정확성을 보장합니다                                                                                  |
| 패딩  | runtime_paddings_t | 네       | 각 차원의 패드 값은 역순으로 표시됩니다. 예를 들어 패드 값은 `[ {2,3}, {1,3} ]`마지막 차원 앞에 패드 2, 뒤에 패드 3. 마지막 2 차원 전면 패드 1, 후면 패드 2 를 나타냅니다 |
| pad_mode | pad_mode_t         | 네       | 현재 const 모드만 지원됩니다                                                                                                                   |
| fill_v   | 뜨다              | 네       | 값을 채웁니다                                                                                                                                     |

**값을 반환합니다**

`result<runtime_tensor>`

**코드 인스턴스입니다**

```cpp
runtime_paddings_t paddings{ { 0, 0 }, { 0, 0 }, { 0, 0 }, { 1, 2 } };
auto output = F::pad(input, paddings, pad_constant, pad_value).unwrap_or_throw();
```
<!-- markdownlint-enable no-emphasis-as-header -->
# 7 정량적 백서

## 7.1 분류 모델 정량화 백서

| 분류 모델입니다     | CPU 정확도(Top-1) | 부동 소수점 정밀도(Top-1) | uint8 정밀도(Top-1) | int8 정확도(Top-1) |
| ------------ | -------------- | --------------- | ---------------- | --------------- |
| 알렉스넷      | 0.531          | 0.53            | 해당 없음              | 0.52            |
| 밀도 121 | 0.732          | 0.732           | 0.723            | 해당 없음             |
| 시작 v3 | 0.766          | 0.765           | 0.773            | 0.77            |
| 시작 v4 | 0.789          | 0.789           | 0.793            | 0.792           |
| 모빌넷 v1 | 0.731          | 0.73            | 0.723            | 0.718           |
| 모빌넷 v2 | 0.713          | 0.715           | 0.713            | 0.719           |
| resnet50 v2  | 0.747          | 0.74            | 0.748            | 0.749           |
| VGG 16       | 0.689          | 0.687           | 0.690            | 0.689           |

> 이 표는 주로 정량적 성능을 비교하기 위한 것으로, cpu 정확도는 전체 ImageNet 유효성 검사 집합 데이터이며, 부동 소수점 및 양자화 정확도는 유효성 검사 집합의 1000 클래스에 대한 데이터 하위 집합 테스트의 결과로 시퀀스 번호에 따라 처음 나타나는 그림입니다.
>
> Alexnet 및 DenseNet의 테스트 결과는 이전 데이터이며 유효성 검사 집합의 처음 1000개 이미지를 데이터의 하위 집합으로 테스트한 결과이며, 해당 당시의 테스트 데이터의 하위 집합은 CPU와 다르므로 비교되지 않습니다.
>
> 선택한 네트워크가 반드시 공식 또는 전처리에서 오는 것은 아니기 때문에 공식 성능과 다를 수 있습니다.

## 7.2 검사 모델 정량화 백서

1. 욜로브3

    | 코코아피                                                      | 공식 결과 | CPU 부동 소수점 정밀도입니다 | gnne 부동 소수점 정밀도입니다 | uint8 정밀도 | int8 정밀도 |
    | ------------------------------------------------------------ | -------- | ----------- | ------------ | --------- | -------- |
    | 평균 정밀도(AP) @ [IoU = 0.50:0.95\| 영역 = 모두 \| 최대 데츠 = 100] | 0.314    | 0.307       | 0.306        | 0.295     | 0.288    |
    | 평균 정밀도(AP) @ [IoU = 0.50\| 영역 = 모두 \| 최대 데츠 = 100] | 0.559    | 0.555       | 0.554        | 0.555     | 0.554    |
    | 평균 정밀도(AP) @ [IoU = 0.75\| 영역 = 모두 \| 최대 데츠 = 100] | 0.318    | 0.308       | 0.307        | 0.287     | 0.275    |
    | 평균 정밀도(AP) @ [IoU = 0.50:0.95\| 영역 = 작음 \| 최대 데츠 = 100] | 0.142    | 0.150       | 0.149        | 0.147     | 0.144    |
    | 평균 정밀도(AP) @ [IoU= 0.50:0.95\| 영역 = 중간 \| 최대 데츠 = 100] | 0.341    | 0.332       | 0.332        | 0.322     | 0.316    |
    | 평균 정밀도(AP) @ [IoU = 0.50:0.95\| 영역 = 큰 \| 최대 데츠 = 100] | 0.464    | 0.437       | 0.437        | 0.414     | 0.404    |
    | 평균 리콜 (AR) @ [IoU= 0.50:0.95\| 영역 = 모두 \| 최대 데트 = 1] | 0.278    | 0.270       | 0.271        | 0.262     | 0.256    |
    | 평균 리콜 (AR) @ [IoU= 0.50:0.95\| 영역 = 모두 \| 최대 데츠 = 10] | 0.419    | 0.412       | 0.412        | 0.399     | 0.392    |
    | 평균 리콜 (AR) @ [IoU = 0.50:0.95\| 영역 = 모두 \| 최대 데츠 = 100] | 0.442    | 0.433       | 0.433        | 0.421     | 0.414    |
    | 평균 리콜 (AR) @ [IoU = 0.50:0.95\| 영역 = 작음 \| 최대 데츠 = 100] | 0.239    | 0.251       | 0.251        | 0.248     | 0.246    |
    | 평균 리콜 (AR) @ [IoU= 0.50:0.95\| 영역 = 중간 \| 최대 데츠 = 100] | 0.482    | 0.462       | 0.463        | 0.451     | 0.443    |
    | 평균 리콜 (AR) @ [IoU = 0.50:0.95\| 영역 = 큰 \| 최대 데츠 = 100] | 0.611    | 0.586       | 0.585        | 0.559     | 0.550    |

2. ssd-mobilenetv1

    | 코코아피                                                                    | 공식 결과 | CPU 부동 소수점 정밀도입니다 | gnne 부동 소수점 정밀도입니다 | uint8 정밀도 | int8 정밀도 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | 평균 정밀도(AP) @ [IoU = 0.50:0.95\| 영역 = 모두 \| 최대 데츠 = 100]   | 0.184    | 0.184       | 0.184        | 0.183     | 0.183    |
    | 평균 정밀도(AP) @ [IoU = 0.50\| 영역 = 모두 \| 최대 데츠 = 100]        | 0.306    | 0.307       | 0.306        | 0.305     | 0.306    |
    | 평균 정밀도(AP) @ [IoU = 0.75\| 영역 = 모두 \| 최대 데츠 = 100]        | 0.191    | 0.192       | 0.190        | 0.189     | 0.190    |
    | 평균 정밀도(AP) @ [IoU = 0.50:0.95\| 영역 = 작음 \| 최대 데츠 = 100] | 0.017    | 0.017       | 0.017        | 0.017     | 0.017    |
    | 평균 정밀도(AP) @ [IoU= 0.50:0.95\| 영역 = 중간 \| 최대 데츠 = 100] | 0.157    | 0.157       | 0.157        | 0.156     | 0.155    |
    | 평균 정밀도(AP) @ [IoU = 0.50:0.95\| 영역 = 큰 \| 최대 데츠 = 100] | 0.371    | 0.372       | 0.371        | 0.370     | 0.369    |
    | 평균 리콜(AR) @ [IoU= 0.50:0.95\| 영역 = 모두 \| 최대 데트 = 1]         | 0.180    | 0.180       | 0.180        | 0.181     | 0.181    |
    | 평균 리콜(AR) @ [IoU= 0.50:0.95\| 영역 = 모두 \| 최대 데츠 = 10]        | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | 평균 리콜(AR) @ [IoU = 0.50:0.95\| 영역 = 모두 \| 최대 데츠 = 100]      | 0.242    | 0.242       | 0.242        | 0.243     | 0.243    |
    | 평균 리콜(AR) @ [IoU = 0.50:0.95\| 영역 = 작음 \| 최대 데츠 = 100]    | 0.026    | 0.026       | 0.026        | 0.026     | 0.026    |
    | 평균 리콜(AR) @ [IoU= 0.50:0.95\| 영역 = 중간 \| 최대 데츠 = 100]    | 0.206    | 0.206       | 0.206        | 0.206     | 0.205    |
    | 평균 리콜(AR) @ [IoU = 0.50:0.95\| 영역 = 큰 \| 최대 데츠 = 100]    | 0.489    | 0.491       | 0.490        | 0.490     | 0.491    |

3. 욜로브5S

    | 코코아피                                                                    | 공식 결과 | CPU 부동 소수점 정밀도입니다 | gnne 부동 소수점 정밀도입니다 | uint8 정밀도 | int8 정밀도 |
    | -------------------------------------------------------------------------- | -------- | ----------- | ------------ | --------- | -------- |
    | 평균 정밀도(AP) @ [IoU = 0.50:0.95\| 영역 = 모두 \| 최대 데츠 = 100]   | 0.367    | 0.365       | 0.335        | 0.334     | 0.335    |
    | 평균 정밀도(AP) @ [IoU = 0.50\| 영역 = 모두 \| 최대 데츠 = 100]        | 0.555    | 0.552       | 0.518        | 0.518     | 0.518    |
    | 평균 정밀도(AP) @ [IoU = 0.75\| 영역 = 모두 \| 최대 데츠 = 100]        | 0.398    | 0.395       | 0.364        | 0.363     | 0.362    |
    | 평균 정밀도(AP) @ [IoU = 0.50:0.95\| 영역 = 작음 \| 최대 데츠 = 100] | 0.223    | 0.220       | 0.199        | 0.199     | 0.197    |
    | 평균 정밀도(AP) @ [IoU= 0.50:0.95\| 영역 = 중간 \| 최대 데츠 = 100] | 0.419    | 0.418       | 0.387        | 0.386     | 0.386    |
    | 평균 정밀도(AP) @ [IoU = 0.50:0.95\| 영역 = 큰 \| 최대 데츠 = 100] | 0.463    | 0.459       | 0.423        | 0.422     | 0.423    |
    | 평균 리콜(AR) @ [IoU= 0.50:0.95\| 영역 = 모두 \| 최대 데트 = 1]         | 0.306    | 0.306       | 0.288        | 0.287     | 0.287    |
    | 평균 리콜(AR) @ [IoU= 0.50:0.95\| 영역 = 모두 \| 최대 데츠 = 10]        | 0.518    | 0.518       | 0.487        | 0.486     | 0.487    |
    | 평균 리콜(AR) @ [IoU = 0.50:0.95\| 영역 = 모두 \| 최대 데츠 = 100]      | 0.576    | 0.576       | 0.540        | 0.539     | 0.540    |
    | 평균 리콜(AR) @ [IoU = 0.50:0.95\| 영역 = 작음 \| 최대 데츠 = 100]    | 0.391    | 0.399       | 0.350        | 0.350     | 0.347    |
    | 평균 리콜(AR) @ [IoU= 0.50:0.95\| 영역 = 중간 \| 최대 데츠 = 100]    | 0.641    | 0.640       | 0.606        | 0.605     | 0.607    |
    | 평균 리콜(AR) @ [IoU = 0.50:0.95\| 영역 = 큰 \| 최대 데츠 = 100]    | 0.716    | 0.710       | 0.680        | 0.683     | 0.685    |

# 8 자주 묻는 질문

1.安装wheel时报错: "xxx.whl은 이 플랫폼에서 지원되는 휠이 아닙니다." **

Q: 安装nncase wheel包, 出现ERROR: nncase-1.0.0.20210830-cp37-cp37m-manylinux_2_24_x86_64.whl은 이 플랫폼에서 지원되는 휠이 아닙니다.

A: 업그레이드 pip > = 20.3

```shell
sudo pip3 install --upgrade pip
```

2.CRB**가 앱 추론 프로그램을 실행할 때 오류 "std::bad_alloc"을 보고합니다**

Q: CRB에서 App 추론 프로그램을 실행 하 고 "std::bad_alloc" 예외를 throw 합니다

```shell
$ ./cpp.sh
case ./yolov3_bfloat16 build at Sep 16 2021 18:12:03
terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc
```

A: std::bad_alloc 예외는 일반적으로 메모리 할당 실패로 인해 발생하며 다음과 같이 해결할 수 있습니다.

- 결과 kmodel이 현재 시스템에서 사용할 수있는 메모리를 초과하는지 확인하십시오 (예 : yolov3 bfloat16 kmodel 크기는 121MB이며 현재 linux에서 사용할 수있는 메모리는 70MB에 불과합니다. 예외가 throw됩니다).  그 이상, 훈련 후 양자화를 사용하여 kmodel 크기를 줄일 수 있습니다.
- 앱에 메모리 누수가 있는지 확인합니다

3. **App 추론 프로그램을 실행할 때[.. t_runtime_tensor.cpp:310 (만들기)] data.size_bytes() = = size = false (bool)**

Q: simulator는 app 추론 프로그램을 실행하여 "[.. t_runtime_tensor.cpp:310 (만들기)]data.size_bytes() == size = false (bool)" 예외를 throw합니다

A: 입력 셰이프 및 요소당 바이트 수(fp32/uint8)에 중점을 두고 설정된 입력 tensor 정보를 확인합니다.

**번역 면책 조항**  
고객의 편의를 위해 Canan은 AI 번역 프로그램을 사용하여 오류를 포함할 수 있는 여러 언어로 텍스트를 번역합니다. 당사는 제공된 번역의 정확성, 신뢰성 또는 적시성을 보장하지 않습니다. Canan은 번역된 정보의 정확성이나 신뢰성에 의존하여 발생하는 손실이나 손해에 대해 책임을 지지 않습니다. 언어 번역 간에 콘텐츠 차이가 있는 경우 중국어 간체 버전이 우선합니다. 

번역 오류 또는 부정확한 문제를 신고하려면 이메일로 문의하시기 바랍니다.