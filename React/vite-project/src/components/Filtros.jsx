import React from 'react'
import { Button } from './button'

export const Filtros = () => {
  return (
    <div className="mb-3 md:flex  md:items-center ">
        <h2 className="dark:text-Neutral-0 text-center text-[2.125rem] font-bold mb-6 md:mb-0 dark:text-white">Extensions List</h2>
      <div className="flex md:flex-col  sm:items-center justify-center   gap-2">
        <Button >All</Button>
        <Button >Active</Button>
        <Button >Inactive</Button>
      </div>

    </div>



        
  )
}
