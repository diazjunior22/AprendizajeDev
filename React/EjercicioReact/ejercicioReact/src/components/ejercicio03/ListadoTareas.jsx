import React , {useState} from 'react'

export const ListadoTareas = () => {
  const [tareas , setTareas] = useState([])
  const [nuevaTarea , setNuevaTarea] = useState('')


  const agregarTarea = () => {
    // copia y se agrega nueva tarea
    setTareas([...tareas, nuevaTarea])
    setNuevaTarea('')


  }
  const eliminarTarea = (indice)  => {
  // filter busca elemento , index z
  const nuevaTarea =  tareas.filter((_, index) => index  !== indice);
  setTareas(nuevaTarea)

}

  return (




    <div>
      
      <h1>ListadoTareas</h1>
      <input type="text"  value={nuevaTarea}  onChange={(e) => setNuevaTarea(e.target.value)
      } />


      <button onClick={agregarTarea}>Agregar TAREA</button>

      <ul>
          {tareas.map((tarea, index) => (
            <li key={index}>
            {tarea}
            {<button onClick={() => eliminarTarea(index)}>Eliminar</button>}
            </li>  )
          )}
      </ul>





    </div>



  )
}
