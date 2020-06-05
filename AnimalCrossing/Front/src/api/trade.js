import { createInstance } from "./index.js";

const instance = createInstance();

/*
 * 해당 카테고리 모든 거래글 가져오기 (동물주민, 미술품, 화석, 기타)
 * 그냥 도감 정보 가져오는 api 가져다 쓰기. 어차피 가져오기만 하는 거니까.
 */

/*
 * 동물주민 카테고리의 특정 id에 대한 모든 거래글 가져오기
 * (예: 동물주민의 id가 1인 모든 거래글)
 */
export function getTradeListAnimalItem(id) {
  return instance
    .get(`/trades/list/animal/${id}`)
    .then(response => {
      console.log(`/trades/list/animal/${id} => `, response.data);
      return response.data;
    })
    .catch(error => {
      console.log(error);
    });
}

/*
 * 미술품 카테고리의 특정 id에 대한 모든 거래글 가져오기
 * (예: 미술품 id가 1인 모든 거래글)
 */
export function getTradeListPaintingItem(id) {
  return instance
    .get(`/trades/list/painting/${id}`)
    .then(response => {
      console.log(`trades/list/painting/${id} => `, response.data);
      return response.data;
    })
    .catch(error => {
      console.log(error);
    });
}

/*
 * 화석 카테고리의 특정 id에 대한 모든 거래글 가져오기
 * (예: 화석 id가 1인 모든 거래글)
 */
export function getTradeListFossilItem(id) {
  return instance
    .get(`/trades/list/fossil/${id}`)
    .then(response => {
      console.log(`trades/list/painting/${id} => `, response.data);
      return response.data;
    })
    .catch(error => {
      console.log(error);
    });
}

/*
 * etc 카테고리의 모든 거래글 리스트 가져오기
 */
export function getTradeListEtc() {
  return instance
    .get("/trades/list/etc/")
    .then(response => {
      console.log("/trades/list/etc/ => ", response.data);
      return response.data;
    })
    .catch(error => {
      console.log(error);
    });
}

/*
 * 특정 거래글로 접근하기
 */
export function getDetailTrade(article_pk) {
  return instance
    .get(`/trades/detail/${article_pk}/`)
    .then(response => {
      console.log(`/trades/detail/${article_pk}/ => `, response.data);
      return response.data;
    })
    .catch(error => {
      console.log(error);
    });
}

/*
 * 특정 거래글로 수정하기
 */
export function updateDetailtrade(article_pk, token) {
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT " + token
  };
  instance
    .put(`trades/detail_ud/${article_pk}/`, article_pk, { headers })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error);
    });
}

/*
 * 특정 거래글로 삭제하기
 */
export function deleteDetailtrade(article_pk, token) {
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT " + token
  };
  instance
    .delete(`trades/detail_ud/${article_pk}/`, article_pk, { headers })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error);
    });
}