![GitHub 릴리즈](https://img.shields.io/github/v/release/IQEngine/IQEngine)
[![Discord](https://img.shields.io/discord/1063315697498853498?label=Discord)](https://discord.gg/k7C8kp3b76)
[![AUR](https://img.shields.io/github/license/IQEngine/IQEngine)](https://github.com/IQEngine/IQEngine/blob/main/LICENSE)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/IQEngine/IQEngine/badge)](https://securityscorecards.dev/viewer/?uri=github.com/IQEngine/IQEngine)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7730/badge)](https://bestpractices.coreinfrastructure.org/projects/7730)
[![Staging](https://img.shields.io/github/actions/workflow/status/IQEngine/IQEngine/periodic_test_of_staging.yml?label=staging)](https://staging.iqengine.org)
[![Prod](https://img.shields.io/github/actions/workflow/status/IQEngine/IQEngine/periodic_test_of_prod.yml?label=prod)](https://iqengine.org)
[![GitHub Sponsors](https://img.shields.io/github/sponsors/IQEngine)](https://github.com/sponsors/IQEngine)

<p align="center">
  <img width=250 src="client/public/IQEngine_Black.svg" />
</p>

<p align="center">[IQEngine](https://www.iqengine.org)을 직접 사용해보세요!</p>
<h4 style="text-align: center;"><i>RF 신호를 분석, 처리 및 공유하기 위한 웹 기반 SDR 도구</i></h4>
* SigMF를 기반으로 하는 스펙트로그램 시각화 및 편집 도구
* RF 기록 파일이나 RFML 데이터셋을 공유하여 상대방이 파일 다운로드나 소프트웨어 설치 없이 확인 가능
* IQEngine은 사용자가 보는 샘플의 일부분만 가져오므로 대규모 RF 기록을 빠르게 탐색 가능
* 신호 감지 알고리즘을 테스트하고 결과를 시각화
* 흥미로운 신호에 푸리에 변환 및 필터를 적용해 인터랙티브 학습
* 메타데이터 검색을 통해 수백만 개의 RF 기록을 체계적으로 관리 및 검색

[GNU Radio](https://www.gnuradio.org/)에서 호스팅하는 [www.iqengine.org](http://iqengine.org/) 공식 인스턴스를 사용해 IQEngine을 체험해보세요. 이 사이트를 통해 로컬 RF 기록을 열어볼 수도 있으며, 모든 처리는 클라이언트 측에서 이루어집니다.

IQEngine은 빠르게 발전 중이며, 매월 업데이트와 새로운 기능, 데모 등을 포함한 이메일 소식을 받아보실 수 있습니다. [여기에서 등록](https://dashboard.mailerlite.com/forms/299501/77960409531811734/share)하세요. 또한 IQEngine [Discord](https://discord.gg/k7C8kp3b76) 채널을 통해 개발에 참여하거나 질문할 수 있습니다.

[라이브 문서](https://staging.iqengine.org/docs)를 확인하거나, 소스 코드의 `client/src/pages/docs/***.mdx` 경로에서 찾을 수 있습니다.

## 주요 기능 목록:

* 줌 및 조정 가능한 스케일을 지원하는 스펙트로그램 + 시간 + 주파수 + IQ 플롯
* 디렉터리 또는 Blob 스토리지 계정에 저장된 RF 기록의 스펙트로그램 썸네일을 포함한 표
* 클라이언트 측에서 수행되는 FIR 필터링 및 FFT 전 임의의 Python 코드 실행
* 플롯/플러그인/다운로드로 전송될 시간 및 주파수 영역 선택 커서
* 구성 가능한 컬러맵
* 전역 파라미터 및 주석을 텍스트나 그래픽으로 편집/보기 가능
* 테이블에서 주석 클릭 시 해당 위치로 바로 이동
* 플러그인을 통해 백엔드에서 DSP 실행 가능 (현재 Python 및 GNU Radio 지원)
* 메타데이터를 데이터베이스로 파싱해 수백만 개의 기록에 대해 검색/질의 가능
* 특정 기록에 대한 액세스를 제어하는 사용자/관리자 시스템
* 새로운 웹 FFT 및 관련 함수 수행을 위한 라이브러리인 [WebFFT](https://www.npmjs.com/package/webfft)를 개발 중이며, 이를 [데모](https://webfft.com/)를 통해 테스트 가능

<p align="center"><img width=250 src="client/public/microsoft-logo.svg" /></p>

<p align="center"><a href="https://www.qoherent.ai/"><img width=250 src="client/public/clogo-black.png" /></a></p>
