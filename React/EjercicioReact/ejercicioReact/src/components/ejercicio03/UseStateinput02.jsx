import React , {useState} from 'react'

export const UseStateinput02 = () => {

    const [numero1, setNumero1] = useState('')
    const [numero2, setNumero2] = useState('')
    const [resultado, setResultado] = useState('')
    const [mensaje, setMensaje] = useState('')


    const calcular = () => {
        const suma = parseFloat(numero1) + parseFloat(numero2)
        setMensaje('La Suma de ' + numero1 + ' y ' + numero2 + ' es: ' + suma)
        setResultado(suma)

        setNumero1('')
        setNumero2('')


    }



  return (
    <div>
        <input type="number" value={numero1} onChange={(e) => setNumero1(e.target.value)}/>
        <input type="number" value={numero2} onChange={(e) => setNumero2(e.target.value)} />

        <button onClick={calcular}>
            Sumar
        </button>


        <p>{mensaje}</p>






    </div>
  )
}
