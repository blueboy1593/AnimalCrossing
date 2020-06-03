<template>
    <!-- 전체 -->
    <div id="writeWrap">

        <!-- 사진 업로드 -->
        <form id="photoUpload" action="" method="">
            <input type="file">
        </form>
            
        <!-- 제목과 내용 -->
        <form id="textUpload" action="" method="">
            <input id="title" type="text" placeholder="제목을 입력해주세요">

            <textarea id="field" placeholder="내용을 입력해주세요">
            </textarea>

            <form id="write" action="">
            <button type="submit">
                <img class="writeButton" src="../../assets/images/write.png" alt="">
            </button>
            </form>
        </form>
    </div>
</template>

<script>
export default {
  name: "write"
}
</script>

<style>
#writeWrap {
    width: 90%;
    height: 350px;
    display: grid;
    grid-template-rows: repeat(2, 1fr);
    grid-template-areas:
        "photoUpload textUpload";
    margin: 0 auto;
    margin-top: 20px;
    display: grid;
    background-color: rgba(53, 238, 29, 0.055);
    border-radius: 30px;
    padding-top: 2.5rem;
}

input:focus {
    outline: none;
}

textarea:focus {
    outline: none;
}

#photoUpload {
    margin: 0 auto;
    min-width: 20%;
    display: grid;
    grid-area: photoUpload;
}

#textUpload {
    min-width: 20%;
    display: grid;
    grid-area: textUpload;
}

#title {
    display: inline-block;
    background-color: rgba(210, 241, 31, 0.37);
    width: 90%;
    height: 50px;
    border-radius: 13px;
}

#field {
    background-color: rgba(210, 241, 31, 0.37);
    width: 90%;
    height: 170px;
    border-radius: 13px;
    margin-top: 10px;
}

#write {
    padding-top: 1rem;
    text-align: center;
}

button {
    outline: 0;
}

.writeButton {
    width: 60px;
}

.writeButton:hover {
    animation: writeButton-ani 1s forwards;
    transform: scale(1.2);
}

@keyframes writeButton-ani {
    0% {
        opacity: 0.8;
        transform: scale(0.95);
    }

    50% {
        opacity: 1;
        transform: scale(1.3);
    }

    100% {
        opacity: 1;
        transform: scale(1.1);
    }
}


@media screen and (max-width: 375px) {
    #writeWrap {
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr);
        grid-template-areas: 
            "photoUpload"
            "textUpload";
    }

}

@media screen and (max-width: 850px) {
    #writeWrap {
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr);
        grid-template-areas: 
            "photoUpload"
            "textUpload";
    }
}

.board__news {
        max-height: 100% !important;
    }

</style>