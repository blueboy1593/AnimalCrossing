import { createInstance } from "./index.js";

const instance = createInstance();

// 모든 자랑 글 가져오기
export function getShows(shows) {
  return instance
    .get("/shows/list/")
    .then(response => {
      shows = response.data;
      console.log("show list", response.data);
      return shows;
    })
    .catch(error => {
      console.log(error);
    });
}
