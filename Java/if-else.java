package AulaIfElse;

import javax.swing.JOptionPane;

public class AulaCondicao {

	public static void main(String[] args) {
        int numero=Integer.parseInt(JOptionPane.showInputDialog("Digite um n�mero"));
        if(numero>=0){
        	JOptionPane.showMessageDialog(null,"O n�mero � positivo");
        }
        else{
        	JOptionPane.showMessageDialog(null, "O n�mero � negativo");
        }
	}
}