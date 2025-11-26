import { useState } from 'react'
import { Headers } from './components/Headers'
import { Filtros } from './components/Filtros'
import { CardContainer } from './components/CardContainer'

function App() {

  return (
  
    <main className='light-gradient  dark:dark-gradient min-h-screen flex flex-col items-center'> 
    {/* my-margen de arriba y abajo */}
    <section className='w-[343px]  my-6' >
      <Headers/>
      <Filtros/>
      <CardContainer/>

    </section>

    </main>
  )
}

export default App
