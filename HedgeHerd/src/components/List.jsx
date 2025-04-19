import React, {useState} from 'react';
import { getFunctions, httpsCallable } from 'frirebase/funcitons'

const ChatGPT = () => {
    const [prompt, setPrompt] = useState('');
    const [output, setOutput] = useState('');
    const [fetching, setFetching] = useState(false);

    const handleSubmit = async () => {
        const funcitons = getFunctions()
        const chatCompletion = httpsCallable(funcitons, 'chatCompletion')
        try {
            const data = {
                prompt
            }
            setFetching(true)
            const result = await chatCompletion(data)
            setOutput(result.data.aiResponse)
        } catch (error) {

        } finally {
            setFetching(false)
        }
    }

    return (
        <div>

        </div>
    )
}