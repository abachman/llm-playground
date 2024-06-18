import { useState } from "react";
import { Message, MessageContent } from "./Message";
import { sendMessage } from "../api/ChatClient";

function createMessage(message: string, author: string): MessageContent {
  return {
    id: Math.random().toString(36).substring(7),
    message,
    author
  }
}

import styles from "./Chat.module.css";

function handleForm(
  evt: React.FormEvent<HTMLFormElement>,
  setMessages: React.Dispatch<React.SetStateAction<MessageContent[]>>
) {
  evt.preventDefault();
  const form = evt.currentTarget;
  const input = form.querySelector("#prompt");
  if (input instanceof HTMLInputElement) {
    const prompt = input.value;
    const botPlaceholder = createMessage("...", "bot");
    setMessages((messages) => {
      return [...messages, createMessage(prompt, "user"), botPlaceholder];
    });
    sendMessage(prompt, botPlaceholder.id).then((response) => {
      const { id, message } = response;

      setMessages((messages) => {
        return messages.map((msg) => {
          if (msg.id === id) {
            return createMessage(message, "bot");
          }
          return msg;
        });
      });
    });
    input.value = "";
  }
}

export const Chat = () => {
  const [messages, setMessages] = useState<MessageContent[]>([
    createMessage(
      `Hello there! I'm FashionBot, your friendly fashion companion.
      I'm excited to chat with you about the latest trends and styles.
      Ask a question to get started!`,
      "bot"
    ),
  ]);

  return (
    <div className={styles.Chat}>
      <div>
        <h1>Little Chatbot</h1>
      </div>
      <div>
        <div>
          {messages.map((message, index) => (
            <Message key={index} message={message} />
          ))}
        </div>
        <form onSubmit={(evt) => handleForm(evt, setMessages)}>
          <div className={styles.Form}>
            <input type="text" name="message" id="prompt" />
            <button type="submit">Send</button>
          </div>
        </form>
      </div>
    </div>
  );
};
