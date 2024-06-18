import styles from "./Chat.module.css";
export type MessageContent = {
  id: string,
  message: string,
  author: string
}

export const Message = ({ message } : { message: MessageContent }) => {
  return (
    <div className={styles.Message}>
      <div className={styles.Actor}>{message.author}</div> <div>{message.message}</div>
    </div>
  )
}