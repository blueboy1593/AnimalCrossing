// userService.js
import { createInstance } from "./index.js";

const instance = createInstance();

function signup(email, nickname, password, success, fail) {
  const user = {
    email: email,
    username: nickname,
    password: password
  };
  instance
    .post("/accounts/signup/", JSON.stringify(user))
    .then(success)
    .catch(fail);
}

function login(email, password, success, fail) {
  const body = {
    email: email,
    password: password
  };

  instance
    .post("/api-token-auth/", JSON.stringify(body))
    .then(success)
    .catch(fail);
}

function findById(id, success, fail) {
  instance
    .get("accounts/userprofile/" + id + "/")
    .then(success)
    .catch(fail);
}

export { signup, login, findById };
