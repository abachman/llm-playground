export type ChatResponse = {
  id: string;
  message: string;
};

export function sendMessage(prompt: string, id: string): Promise<ChatResponse> {
  return fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ prompt, id }),
  })
    .then((response) => response.json())
    .then((data) => ({
      message: data.response,
      id: data.id,
    }));

  // return new Promise((resolve) => {
  //   setTimeout(() => {
  //     resolve({
  //       message: `THE PROMPT WAS: ${prompt}`
  //     })
  //   }, 1000)
  // })
}
