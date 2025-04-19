const functions = require("firebase-functions");
const admin = require("firebase-admin");
const OpenAi = require("openai")

if (admin.apps.length === 0) {
    admin.initializeApp();
}

exports.chatCompletion = functions.https.onCall(async (data, context) => {
    const { prompt } = data;

    const openai = new OpenAi({
        apiKey: process.env.OPENAI_API_KEY
    });
    
    const aiModel = "gpt-4.1-nano"

    const messages = [
        {
            role:"system",
            content:"you are a helpful assistant"
        },
        {
            role:"user",
            content:prompt
        },
    ]

    const completion = await openai.chat.completions.create({
        model: aiModel,
        messages: messages
    })

    const aiResponse = completion.choices[0].message.content

    return {
        aiResponse
    }
})
