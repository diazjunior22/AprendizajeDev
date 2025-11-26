import React from 'react'
import { Button } from './button'
import { Toggle } from 'rsuite';
import 'rsuite/Toggle/styles/index.css';


export const Card = ({name, logo, description, isActive}) => {
  return (
    <div className='bg-red-800 p-4  rounded-lg '>

        <div className='flex gap-1 text-white '>
        <img src={logo} alt="logo" />
        <div>
        <h2>{name}</h2>
        <p>{description}</p>
        </div>
        </div>
        <div className='flex  justify-end gap-4 items-center'>
        <Button className="bg-white">
            ACTIVE
        </Button>
    <Toggle color='red'/>
        </div>



        
    </div>
  )
}


