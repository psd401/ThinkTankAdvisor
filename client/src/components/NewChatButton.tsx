import React from "react";
import {chatItem} from "./LiveChatFeed";

interface Props {
    setCurrentChat: React.SetStateAction<any>
    previousChats: Array<Array<chatItem>>
    setPreviousChats: React.SetStateAction<any>
    currentChat: Array<chatItem>
}


function NewChatButton({setCurrentChat, previousChats, setPreviousChats, currentChat}: Props) {
    const createNewChat = () => {
        setPreviousChats(
            [
                ...previousChats,
                currentChat
            ]
        )
        setCurrentChat([
            {
                "text": "Howdy, I'm a chatbot which leverages the gpt-3.5-turbo model. But " +
                    "the context for my responses comes from a semantic search performed against a vector database " +
                    "of youtube video transcripts using your questions. Currently I can only answer questions on the videos from " +
                    "this here playlist: ",
                "isBot": true
            }
        ])
    }

    return (
        <button
            id="new-chat-button"
            onClick={() => {createNewChat()}}
        > + New Chat
        </button>
    )
}

export default NewChatButton
