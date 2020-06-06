import { createInstance } from "./index.js";

const instance = createInstance();

// 모든 자랑 글 가져오기
export function getShows(shows) {
  return instance
    .get("/shows/list/")
    .then(response => {
      shows = response.data;
      // console.log("show list", response.data);
      return shows;
    })
    .catch(error => {
      console.log(error);
    });
}

export function getShowById(showId, data) {
  return instance
    .get(`/shows/detail/${showId}/`)
    .then(response => {
      data = response.data;
      // console.log(data);
      return data;
    })
    .catch(error => {
      console.log(error);
    });
}

// 자랑글 쓰기
export function writeShows(article, token) {
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT " + token
  };
  instance
    .post("/shows/write/", article, { headers })
    .then(response => {
      console.log("show write", response.data);
    })
    .catch(error => {
      console.log(error);
    });
}

// 자랑글 삭제하기
export function deleteShows(show_pk, token) {
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT " + token
  };
  instance
    .delete(`/shows/detail_ud/${show_pk}/`, show_pk, { headers })
    .then(response => {
      this.$router.go(-1);
      console.log("삭제완료:::: ", response.data);
    })
    .catch(error => {
      console.log(error);
    });
}

// Show 게시판에서 댓글 달기
export function writeComment(comment, show_id, token) {
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT " + token
  };
  instance
    .post(`/shows/comment/${show_id}/`, comment, { headers })
    .then(response => {
      console.log("show comment 작성!!!", response.data);
    })
    .catch(error => {
      console.log(error);
    });
}
