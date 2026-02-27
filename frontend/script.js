const API_URL = "http://127.0.0.1:8000";

// ================= DARK MODE =================
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

// ================= LOGOUT =================
function logout() {
    window.location.href = "login.html";
}

// ================= LOGIN =================
async function login() {

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    });

    const data = await response.json();

    console.log("STATUS:", response.status);
    console.log("DATA:", data);

    if (response.status === 200) {
        alert("Login successful");
        window.location.href = "grammar.html";
    } else {
        alert("Login failed");
    }
}



// ================= REGISTER =================
async function register() {

    const name = document.getElementById("registerName").value;
    const email = document.getElementById("registerEmail").value;
    const password = document.getElementById("registerPassword").value;

    if (!name || !email || !password) {
        alert("Please fill all fields");
        return;
    }

    const response = await fetch(`${API_URL}/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            email: email,
            password: password
        })
    });

    const data = await response.json();

    if (response.ok) {
        alert("Registration successful!");
        window.location.href = "login.html";
    } else {
        alert(data.detail || "Registration failed");
    }
}

// ================= CHECK GRAMMAR =================
async function checkGrammar() {

    const textInput = document.getElementById("text");

    if (!textInput) return;

    const text = textInput.value;

    if (!text) {
        alert("Enter text first");
        return;
    }

    try {
        const response = await fetch(`${API_URL}/check-grammar`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        // -------- Corrected Text --------
        const correctedBox = document.getElementById("correctedText");
        if (correctedBox)
            correctedBox.innerText = data.corrected_text;

        // -------- Highlighted Errors --------
        // -------- Highlighted Errors (SAFE VERSION) --------
        let highlightedText = text;

        data.errors.forEach(err => {
            const escapedWord = err.incorrect_text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

            const regex = new RegExp(`\\b${escapedWord}\\b`, "gi");

            highlightedText = highlightedText.replace(regex, match =>
                `<span class="error-highlight">${match}</span>`
            );
        });

        document.getElementById("highlightedText").innerHTML = highlightedText;


        // -------- Error List --------
        const errorList = document.getElementById("errorList");
        if (errorList) {
            errorList.innerHTML = "";

            data.errors.forEach(err => {
                const li = document.createElement("li");
                li.innerText =
                    `Incorrect: "${err.incorrect_text}" - Suggestions: ${err.suggestions.join(", ")}`
                errorList.appendChild(li);
            });
        }

        // -------- Grammar Score --------
        const wordCount = text.split(/\s+/).length;
        const errorCount = data.total_errors;

        let score = Math.max(0, Math.round(((wordCount - errorCount) / wordCount) * 100));

        const scoreFill = document.getElementById("scoreFill");
        if (scoreFill) {
            scoreFill.style.width = score + "%";
            scoreFill.innerText = score + "%";
        }

    } catch (error) {
        alert("Grammar check failed");
        console.error(error);
    }
}
