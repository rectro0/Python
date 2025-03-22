import { useState , useEffect} from 'react'
import viteLogo from '/vite.svg'
import ContactLList from './ContactLList'
import './App.css'





function App() {
  
  const [contacts , setContacts] = useState([])

  useEffect(() => {
    fetchContact()
  }, [])

  const fetchContact = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)

  }

  return <><ContactLList contacts={contacts}/>
  <ContactForm/></>
}

export default App
