import React, { useState } from 'react'
import logo from '../assets/img/images/logo.svg'
import darkicon from '../assets/img/images/icon-moon.svg'
import sunIcon from '../assets/img/images/icon-sun.svg'
import  logoDark from '../assets/img/images/logo-dark.svg'

import '../index.css'



export const Headers = () => {
      const saveTheme = localStorage.getItem('dark')
      const [isDark, setIsDark] = useState((JSON.parse(saveTheme)) || false)

      if (JSON.parse(saveTheme)){
      document.documentElement.classList.add('dark')
    };
  
  const handleClick = () => {
    // setImg(img === darkicon ?  logo : darkicon)
      const isDarkChanged = document.documentElement.classList.toggle('dark')
      setIsDark(!isDark);
      localStorage.setItem('dark', !isDark);



    

  }




  return (
    // px padding  
    <div className='bg-Neutral ligth-gradient dark:Neutral-800  border-2 h-[66px] flex justify-between  px-3 py-2 rounded-[10px] items-center'>
              <img src={isDark ? logoDark : logo} alt="logo" />
                    <button onClick={handleClick} className='bg-neutral-100  cursor-pointer  size[70px] grid place-content-center rounded-full py-2 px-2'>
                          <img src={isDark ? darkicon : sunIcon } alt="logo"  />
                    </button>




    </div>
  )
}
