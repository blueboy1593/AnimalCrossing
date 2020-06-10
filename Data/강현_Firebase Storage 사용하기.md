# Firebase Storage 사용하기

1. 프로젝트 새로 생성하기.

   여기는 따로 가이드라인 없이 Firebase 홈페이지에서 그냥 시키는대로 추가해주면 됨.

![pjt_add](firebase_assets\pjt_add.PNG)

2. Practice로 만들어보기

   <img src="firebase_assets\practice_make.PNG" alt="practice_make" style="zoom:60%;" />

3. 웹에 firebase 추가하기

   앱 등록 닉네임은 마음대로 설정해주면 된다.

   <img src="firebase_assets\web_add.PNG" alt="web_add" style="zoom:60%;" />

4. 아래에 보이는 키는 복사를 해서 붙여넣기를 해야하는 곳!

   쉽게 설명하면 내 firebase storage의 주소와 나의 apikey 등 접근할 수 있는 권한 정보들이 모두 들어있다.

<img src="firebase_assets\script.PNG" alt="script" style="zoom:60%;" />

5. 사진을 저장할 스토리지를 사용할 예정이기에 스토리지를 시작하자.

<img src="firebase_assets\storage_start.PNG" alt="storage_start" style="zoom:50%;" />

6. asia-east2 같은 지역으로 설정해준다.

7. Rules가

   ```
   rules_version = '2';
   service firebase.storage {
     match /b/{bucket}/o {
       match /{allPaths=**} {
         allow read, write: if request.auth != null;
       }
     }
   }
   
   이렇게 되어있는데
   ```

   ```
   rules_version = '2';
   service firebase.storage {
     match /b/{bucket}/o {
       match /{allPaths=**} {
         allow read, write:
       }
     }
   }
   ```

    if request.auth != null; 요부분을 제거해준다. 누구나 allow 한다는 뜻

8. Vue의 main.js에 써줄 코드

   ```js
   // firebase 사용
   import * as firebase from "firebase";
   
   var firebaseConfig = {
     apiKey: "AIzaSyDJ_cU7yM-78IESIAIj7Pj4d8iHkFqJxp4",
     authDomain: "modong-158aa.firebaseapp.com",
     databaseURL: "https://modong-158aa.firebaseio.com",
     projectId: "modong-158aa",
     storageBucket: "modong-158aa.appspot.com",
     messagingSenderId: "753568862888",
     appId: "1:753568862888:web:488d24c4bd8d67aa73a89d",
     measurementId: "G-3PWVWWLPVJ"
   };
   
   firebase.initializeApp(firebaseConfig);
   firebase.analytics();
   ```

9. npm i firebase

   ```bash
   npm install firebase
   ```

10. 이런식으로 클라우드에 저장하고 불러오게 활용 가능.

    ```vue
    <script>
    import * as firebase from "firebase";
    
        async onChangeImages(e) {
          console.log(e.target.files);
          const file = e.target.files[0];
          this.article.imageUrl = URL.createObjectURL(file);
          await firebase
            .storage()
            .ref()
            .child(file.name)
            .put(file)
            .then(response => {
              console.log(response);
              console.log("firebase 업로드");
            });
          let image = "";
          await firebase
            .storage()
            .ref()
            .child(file.name)
            .getDownloadURL()
            .then(response => {
              console.log(response);
              console.log("firebase 받아오기");
              image = response;
            });
          this.article.imageUrl = image;
        },
    </script>
    ```

    

