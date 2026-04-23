import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [items, setItems] = useState([])
  
  // Use environment variable for the API URL, default to localhost for local dev
  const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'

  useEffect(() => {
    axios.get(`${API_URL}/items`)
      .then(response => setItems(response.data))
      .catch(error => console.error("Error fetching data:", error))
  }, [])

  return (
    <div style={{ padding: '20px' }}>
      <h1>My SaaS Dashboard</h1>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  )
}

export default App