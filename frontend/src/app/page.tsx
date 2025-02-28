
export default function Home() {
  return (
    fetch("http://127.0.0.1:8000/api/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: "Your long text here" })
  })
  .then(response => response.json())
  .then(data => console.log("Summary:", data.result))
  .catch(error => console.error("Error:", error))
  )
}
