const registerForm = document.getElementById("registerForm");

const childrens = registerForm.childNodes;

let [emailValidate, passwordValidate] = [false, false];
childrens.forEach((child) => {
  if (child.nodeName == "INPUT") {
    if (child.getAttribute("name") == "email") {
      child.addEventListener("input", (e) => {
        let email = e.target.value;
        if (email.includes("@") && email.includes(".com")) {
          emailValidate = true;
          child.setCustomValidity("");
        } else {
          emailValidate = false;
          child.setCustomValidity("Please enter a valid email address.");
        }
      });
    }
  }
});
