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
      console.log(data);
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
