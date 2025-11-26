import React , {useState} from 'react'
import { Login } from './login'
import { Logout } from './logout'
export const Session = () => {
    const [isLoggedIn , setIsloggedIn] = useState(true)

  return (
    <div>
        {isLoggedIn ? <Logout/> : <Login/>}
        <button onClick={() => setIsloggedIn(!isLoggedIn)}> {isLoggedIn ?"CERRAR SESSION" : 'INICIA SESSION'}</button>
    </div>
  )
}
