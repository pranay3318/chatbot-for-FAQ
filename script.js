const chatArea =
document.getElementById("chatArea");

const userInput =
document.getElementById("userInput");

const sendBtn =
document.getElementById("sendBtn");

sendBtn.addEventListener(
    "click",
    sendMessage
);

userInput.addEventListener(
    "keypress",
    function(event){

        if(event.key === "Enter"){
            sendMessage();
        }

    }
);

function sendMessage(){

    const text =
    userInput.value.trim();

    if(text === "") return;

    addMessage(
        "You",
        text
    );

    let response =
    getResponse(text);

    setTimeout(() => {

        addMessage(
            "Bot",
            response
        );

    },1000);

    userInput.value = "";
}

function addMessage(sender,message){

    chatArea.innerHTML +=
    `
    <p>
    <b>${sender}:</b>
    ${message}
    </p>
    <br>
    `;

    chatArea.scrollTop =
    chatArea.scrollHeight;
}

function getResponse(text){

    text = text.toLowerCase();

    if(text.includes("hello"))
        return "Hello!";

    if(text.includes("how are you"))
        return "I am doing great!";

    if(text.includes("your name"))
        return "I am an AI Chatbot.";

    if(text.includes("ipl"))
        return "Royal challengers bangalore(RCB).";

    if(text.includes("india"))
        return "India is a country in South Asia.";
    if(text.includes("lbrce"))
        return "LBRCE is an institution in mylavaram.";
    if(text.includes("ai"))
        return "Artificial Intelligence is the simulation of human intelligence processes by machines.";

    return "Sorry, I don't know that yet.";
}