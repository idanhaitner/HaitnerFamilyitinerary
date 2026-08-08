/* Soft client-side gate — keeps casual visitors out */
(function () {
  const STORAGE_KEY = "haitner-japan-2026:unlocked";
  const PASS_HASH = "b181ca2307e6900f3d218dcabd221d64d0296cffbac6fa70a89815e67a3a49b1";

  const gate = document.getElementById("site-gate");
  const form = document.getElementById("gate-form");
  const input = document.getElementById("gate-password");
  const error = document.getElementById("gate-error");
  const card = gate && gate.querySelector(".site-gate-card");

  async function sha256(text) {
    if (!window.crypto || !crypto.subtle) {
      return null;
    }
    const data = new TextEncoder().encode(text);
    const buf = await crypto.subtle.digest("SHA-256", data);
    return Array.from(new Uint8Array(buf))
      .map((b) => b.toString(16).padStart(2, "0"))
      .join("");
  }

  function finishUnlock() {
    document.body.classList.remove("site-locked");
    if (gate) {
      gate.hidden = true;
      gate.setAttribute("aria-hidden", "true");
      gate.classList.remove("is-unlocking");
    }
  }

  function unlock(animated) {
    try {
      localStorage.setItem(STORAGE_KEY, "1");
    } catch (_) {
      /* ignore */
    }

    if (!animated || !gate || window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      finishUnlock();
      return;
    }

    gate.classList.remove("is-shaking");
    gate.classList.add("is-unlocking");
    if (card) card.classList.add("is-unlocking");

    const done = () => {
      gate.removeEventListener("animationend", onEnd);
      finishUnlock();
    };
    const onEnd = (e) => {
      if (e.target === gate) done();
    };
    gate.addEventListener("animationend", onEnd);
    setTimeout(done, 700);
  }

  function showError(msg) {
    if (!error) return;
    error.textContent = msg;
    error.hidden = !msg;
  }

  function shakeWrong() {
    if (!gate || !card) return;
    gate.classList.remove("is-shaking");
    card.classList.remove("is-shaking");
    input.classList.remove("is-wrong");
    void gate.offsetWidth;
    gate.classList.add("is-shaking");
    card.classList.add("is-shaking");
    input.classList.add("is-wrong");
    const clear = () => {
      gate.classList.remove("is-shaking");
      card.classList.remove("is-shaking");
      input.classList.remove("is-wrong");
      card.removeEventListener("animationend", clear);
    };
    card.addEventListener("animationend", clear);
  }

  try {
    if (localStorage.getItem(STORAGE_KEY) === "1") {
      unlock(false);
      return;
    }
  } catch (_) {
    /* ignore */
  }

  if (!form || !input) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    showError("");
    const value = (input.value || "").trim();
    if (!value) {
      showError("נא להזין סיסמה");
      shakeWrong();
      input.focus();
      return;
    }

    const hashed = await sha256(value);
    if (hashed && hashed === PASS_HASH) {
      showError("");
      form.classList.add("is-success");
      unlock(true);
      return;
    }

    showError("סיסמה שגויה");
    shakeWrong();
    input.value = "";
    input.focus();
  });

  input.focus();
})();
