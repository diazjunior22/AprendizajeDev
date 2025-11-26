import React from 'react'


export const Button = ({children}) => {
  return (
    <button className='border   font-bold border-Neutral-300 px-5 py-2 rounded-full flex items-center justify-center hover:border-Neutral-900 hover:bg-red-900
     hover:bg-Neutral-100 hover:text-Neutral-900  cursor-pointer
    dark:hover:bg-Neutral-600  dark:hover:bg-red-500   dark:text-white   dark:border-Neutral-600

    
    '>{children}</button>
  )
}
