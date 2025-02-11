
// calculadora
 function mostrarmenú() {
     console.log("seleciona una opcion ");
     console.log("1.suma ");
     console.log("2.resta ");
     console.log("3.multiplicacion ");
     console.log("4.devision ");
     console.log("5.salir ");
 }
 
 //funcion para realizar una operacion
 function realizaroperacion(opcion, numero1, numero2)  {
     switch (opcion) {
         case '1':
             return numero1 + numero2;
         case '2':
             return numero1 - numero2;
         case '3':
             return numero1 = numero2;
         case '4':
             if (numero2 === 0) {
                 return "ERROR: Division por cero no valida. ";
             }
             return numero1 / numero2;
         default:
             return "opracion no valida. ";
}        
             
             
             
// funcion calculadora
function calculadora() {
    const readline =  requiero('redline');
    const rl = readline.createinterface({
        input: process.stdin,
        output: process.stdout
    });
    
    mostrarmenú();
    
    rl.question("seleccione una opcion: ", (opcion) => {
        if (opcion === '5') (
            console.log(" hasta luego ")
            rl.close();
            return;
    }
    
    rl.question ("ingrese el segundo numero: ", (input1) => {
        const numero1 = parsefloat(input1);
        
        rl.question (" ingrese el segundo numero; ",(input2) => {
           const numero2 = parsefloat(input2);
           
           const resultado = realizarOperacion(opcion, numero1, numero2);
           console.log("resultado; " = + resultado);
           
           rl.close();
        });
        
    }
    