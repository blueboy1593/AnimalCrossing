import { createInstance } from "./index.js";

const instance = createInstance();

// 모든 트레이드 글 가져오기
export function getTrades(trades) {
  return instance
    .get("/trades/list/")
    .then(response => {
      trades = response.data;
      return trades;
    })
    .catch(error => {
      console.log(error);
    });
}

// 특정 id에 대한 거래글 모두 가져오기

export function getTradeById(category, id, lists) {
  return instance
    .get(`/trades/list/${category}/${id}/`)
    .then(response => {
      lists = response.data;
      return lists;
    })
    .catch(error => {
      console.log(error);
    });
}

/*
 * 해당 카테고리 모든 거래글 가져오기 (동물주민, 미술품, 화석, 기타)
 * 그냥 도감 정보 가져오는 api 가져다 쓰기. 어차피 가져오기만 하는 거니까.
 */

/*
 * etc 카테고리의 모든 거래글 리스트 가져오기
 */
export function getTradeListEtc() {
  return instance
    .get("/trades/list/etc/")
    .then(response => {
      return response.data;
    })
    .catch(error => {
      console.log(error);
    });
}

/*
 * 특정 거래글로 접근하기
 */
export function getDetailTradeByArticleId(tradeId, data) {
  return instance
    .get(`/trades/detail/${tradeId}/`)
    .then(response => {
      data = response.data;
      return data;
    })
    .catch(error => {
      console.log(error);
    });
}

// 거래글 작성하기

export function tradePost(trade, token, success, fail) {
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT " + token
  };
  instance
    .post("/trades/write/", trade, { headers })
    .then(success)
    .catch(fail);
}

/*
 * 특정 거래글로 수정하기
 */
export function updateDetailtrade(article_pk, token, success, fail) {
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT " + token
  };
  instance
    .put(`trades/detail_ud/${article_pk}/`, article_pk, { headers })
    .then(success)
    .catch(fail);
}

/*
 * 특정 거래글로 삭제하기
 */
export function deleteArticleApi(article_pk, token, success, fail) {
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT " + token
  };
  instance
    .delete(`trades/detail_ud/${article_pk}/`, { headers })
    .then(success)
    .catch(fail);
}

// 댓글 작성하기
export function writeComment(comment, article_pk, token, success, fail) {
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT " + token
  };
  instance
    .post(`/trades/comment/${article_pk}/`, comment, { headers })
    .then(success)
    .catch(fail);
}
// 댓글 삭제하기
export function deleteCommentApi(comment_pk, token, success, fail) {
  const headers = {
    "Content-Type": "application/json",
    Authorization: "JWT " + token
  };
  instance
    .delete(`/trades/comment_ud/${comment_pk}/`, { headers })
    .then(success)
    .catch(fail);
}
