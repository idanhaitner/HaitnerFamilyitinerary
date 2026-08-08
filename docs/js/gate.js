/* Soft client-side gate — keeps casual visitors out */
(function () {
  const STORAGE_KEY = "haitner-japan-2026:unlocked";
  const PASS_HASH = "b181ca2307e6900f3d218dcabd221d64d0296cffbac6fa70a89815e67a3a49b1";

  const gate = document.getElementById("site-gate");
  const form = document.getElementById("gate-form");
  const input = document.getElementById("gate-password");
  const error = document.getElementById("gate-error");

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

  function unlock() {
    try {
      localStorage.setItem(STORAGE_KEY, "1");
    } catch (_) {
      /* ignore */
    }
    document.body.classList.remove("site-locked");
    if (gate) {
      gate.hidden = true;
      gate.setAttribute("aria-hidden", "true");
    }
  }

  function showError(msg) {
    if (!error) return;
    error.textContent = msg;
    error.hidden = !msg;
  }

  try {
    if (localStorage.getItem(STORAGE_KEY) === "1") {
      unlock();
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
      input.focus();
      return;
    }

    const hashed = await sha256(value);
    if (hashed && hashed === PASS_HASH) {
      unlock();
      return;
    }

    showError("סיסמה שגויה");
    input.value = "";
    input.focus();
  });

  input.focus();
})();
