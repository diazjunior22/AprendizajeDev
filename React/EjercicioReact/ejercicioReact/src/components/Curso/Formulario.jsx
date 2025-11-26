import React , {useState} from 'react'

export const Formulario = () => {
    const [formData, setFormData] = useState({nombre : '' , apellido : ''})

    const manejarCambios = (evento) => {
        const {name , value} = evento.target;
        setFormData(prevState => (
          {
            ...prevState,
            [name] : value
          }
        ))

    }

    const manejarSudmit = (evento) => {
      // para no recargar el formulario
      evento.preventDefault();  
      console.log(formData)
    }


  return (
    <form onSubmit={manejarSudmit}>
        Formulario CON UN SOLO USE STATED
        <input type="text"  name='nombre' placeholder='Escribe Tu Nombre'  value={formData.nombre}  onChange={manejarCambios} />
        <input type="text"  name='apellido' placeholder='Escribe Tu Apellido'  value={formData.apellido}  onChange={manejarCambios}/>
        <p>MI NOMBRE ES {formData.nombre} {formData.apellido}</p>
        <button type='submit'>Enviar Formulario</button>


    </form>
  )
}
