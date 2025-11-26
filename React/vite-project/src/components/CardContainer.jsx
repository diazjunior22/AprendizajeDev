import React from 'react'
import data from '../../data.json'
import { Card } from './Card'


export const CardContainer = () => {
  return (
    <div className='flex-col justify-center items-center flex  gap-10  '>
     {/* {data.map(insertion => <Card key={insertion.name} name={insertion.name} logo={insertion.logo} description={insertion.description} isActive={insertion.isActive}/>)} */}
    {data.map(insertion => <Card key={insertion.name} {...insertion}/>)}

    </div>
  )
}
