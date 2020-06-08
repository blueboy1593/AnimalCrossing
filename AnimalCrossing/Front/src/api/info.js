import { createInstance } from "./index.js";

const instance = createInstance();

// 물고기 도감 정보 가져오기
export function getFishes(cards) {
  return instance
    .get("/api/v1/fishes/")
    .then(response => {
      cards = response.data;
      // console.log("response.data::::  ", response.data);
      return cards;
    })
    .catch(error => {
      console.log(error);
    });
}

// 곤충 도감 정보 가져오기
export function getInsects(cards) {
  return instance
    .get("/api/v1/insects/")
    .then(response => {
      cards = response.data;
      return cards;
    })
    .catch(error => {
      console.log(error);
    });
}

// 화석 도감 정보 가져오기
export function getFossils(cards) {
  return instance
    .get("/api/v1/fossils/")
    .then(response => {
      cards = response.data;
      // console.log("response.data::::  ", response.data);
      return cards;
    })
    .catch(error => {
      console.log(error);
    });
}

// 동물주민 도감 정보 가져오기
export function getNeighbors(cards) {
  return instance
    .get("/api/v1/animals/")
    .then(response => {
      cards = response.data;
      return cards;
    })
    .catch(error => {
      console.log(error);
    });
}

// 미술작품 도감 정보 가져오기
export function getPaintings(cards) {
  return instance
    .get("/api/v1/paintings/")
    .then(response => {
      cards = response.data;
      // console.log("response.data::::  ", response.data);
      return cards;
    })
    .catch(error => {
      console.log(error);
    });
}
