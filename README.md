# 1. spartamarket v.0.1 (with DRF)

- [1. spartamarket v.0.1 (with DRF)](#1-spartamarket-v01-with-drf)
  - [1.1. Overview](#11-overview)
  - [1.2. 진행 상황](#12-진행-상황)
  - [1.3. ERD](#13-erd)
  - [1.4. API Documents](#14-api-documents)
  - [1.5. 이슈 정리](#15-이슈-정리)
    - [1.5.1. API 설계 이슈](#151-api-설계-이슈)
    - [1.5.2. ViewSet 이슈](#152-viewset-이슈)
    - [1.5.3. Pagination 이슈](#153-pagination-이슈)
    - [1.5.4. Permission 이슈](#154-permission-이슈)
    - [1.5.5. **ORM 이슈**](#155-orm-이슈)
    - [1.5.6. **Custom User 이슈**](#156-custom-user-이슈)

<br>
<br>

## 1.1. Overview

- **참여자** : 이윤후
- **기간** : 24.05.01~02
- **목표** : DRF를 이용해서 회원가입, 로그인, CRUD를 할 수 있는 API 생성
- **사용한 서드파티 앱** :
   - django_extensions, django_seed, drf_spectacular
   - requirements.txt 참고
- **이슈** : Pagination, Custom User, ORM 등에서 간단한 이슈들이 있었음

<br>
<br>

## 1.2. 진행 상황
   - 완료 : ERD 작성, 회원가입, 로그인, 프로필 조회, 상품 목록 조회, 페이지네이션, 상품 등록/수정/삭제, 로그아웃
   - 진행예정 :  API 설계서 작성, 상품 조회, 유저 팔로잉 기능, 상품 search, 게시글 좋아요, 상품 태그, 프로필 수정, 패스워드 변경, 회원 탈퇴
   - 자세한 현재 진행 상황은 kanban board은 참고
   - https://github.com/users/quasar2yh/projects/2/views/1
   - ![image](https://github.com/quasar2yh/django_drf/assets/58003233/4d847538-79b5-419b-acb8-02b926029c22)

 <br>
 <br>
 <br>
 <br>

## 1.3. ERD

[<image src="https://github.com/quasar2yh/django_drf/assets/58003233/7b97a07c-1f90-433e-b713-bd86b1daed26" style="width: 808px; height: 550px;">]((https://dbdiagram.io/d/market-660a60a937b7e33fd72ff8c0))
<br>
[ERD page](https://dbdiagram.io/d/market-660a60a937b7e33fd72ff8c0)
 <br>
 <br>
 <br>
 <br>
 

## 1.4. API Documents

   -  ![image](https://github.com/quasar2yh/django_drf/assets/58003233/00d2eabc-7bf2-4903-8274-2e839e6c868e)
   - 아래 버튼을 클릭하면 API 문서를 Fork 하셔서 가져가실 수 있습니다.

  [<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/24074190-c44e384d-2119-481e-8900-66d1f6d5b03b?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D24074190-c44e384d-2119-481e-8900-66d1f6d5b03b%26entityType%3Dcollection%26workspaceId%3D03b015f4-d50e-4fe3-8cf6-d38ba7412daf)

 <br>
 <br>
 <br>
 <br>


 ## 1.5. 이슈 정리
 원래 개발하면서 발생한 이슈는 Issue 게시판에 올리지만 첫 DRF 프로젝트인 만큼 개발 과정에서 있던 이슈 상황을 간략하게 정리하고 싶었습니다.

 <br>
 <br>

 처음이니만큼 초보적인 실수도 존재했으며, 간단한 기능구현에도 시간이 꽤 걸린 경우가 있었습니다. 하지만 진짜 문제는 미약한 실력이 아닌 반복적인 실수와 나아지지 않는 실력이기에 지금은 비록 하찮은 이슈사항일지라도 여기에 정리해보았습니다.

 <br>
 <br>

### 1.5.1. API 설계 이슈
- **Way I used** : 하루만에 기능을 구현하려고 API 설계를 따로 정리하지 않았음
- **Recommend** : 간단한 기능구현만 있는 프로젝트라도 추가적인 요구사항이 생길 경우, API 설계가 제대로 잡혀있지 않다면 API가 뒤죽박죽 될 가능성이 존재함. 꼭 API 설계부터 시작하기

 <br>
 <br>
 
### 1.5.2. ViewSet 이슈
- **Way I used** :
   - FBV, APIView, ViewSet을 공부해보았고 그중 ViewSet 방식을 사용해 봄.
   - ViewSet이 추상화가 잘 되어있어서 View 쪽에서의 메인 비즈니스 로직 구현과 관리가 쉬웠음.
   - 간단한 CRUD 요구사항에서는 높은 생산성을 보임.
   - 하지만 추가적인 요구사항이나 틀에서 벗어난 기능 구현에서는 살짝 복잡해지는 경우가 존재했음.
- **Recommend** : FBV, APIView, ViewSet, GenericView, Mixin 모든 방식을 기본적인 수준에서는 숙지하고 비즈니스 상황에 따라 적용하면 좋을 것 같음 

 <br>
 <br>

### 1.5.3. Pagination 이슈
- **Way I used** : ViewSet 방식을 이용했기에 Pagination 구현이 어렵지 않았음.
- **Recommend** :  CBV 방식에 따른 pagination 방법이 다르고 PageNumberpagination, CursurPagination 등과 같이 pagination의 종류도 몇 가지 있는 것을 알게 됨. 추가적인 문서 리딩이 필요함

 <br>
 <br>

### 1.5.4. Permission 이슈
- **Way I used** : 장고에서 제공하는 permission인 IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny 를 사용
- **Recommend** :
   - AllowAny보다는 안전한 Method의 요청만 승인하는 IsAuthenticatedOrReadOnly이 권장됨.
   - 추후에 비즈니스 상황에 따라 다양한 permission 유형이 필요할 수 있음
   - 이에 따라 Permission custumize 방법도 공부할 필요가 있음

 <br>
 <br>

### 1.5.5. **ORM 이슈**

- **Way I used** : object.get()과 get_object_or_404()를 혼용함
- **Recommend** : DB에서 해당 값을 못 찾아서 발생하는 에러를 따로 처리해줄 것이 아니라면 get_object_or_404()사용하는 것을 권장

 <br>
 <br>

  ### 1.5.6. **Custom User 이슈**
- **Way I used** :
   - 커스텀 유저 모델과 유저 시리얼라이져 사용
   - 시리얼라이져에 validate_password() 이용해서 암호를 해시화
- **Recommend** :
   - **유저 모델은 get_user_model() 을 사용하는 것을 권장**
   - 시리얼라이져에서도 유저 모델을 가져올 때 get_user_model()을 사용할 수 있음
 <br>
 
 
 ``` python
class UserSerilizer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
```

 <br>
 <br>
 































 
