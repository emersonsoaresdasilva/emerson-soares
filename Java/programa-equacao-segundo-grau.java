import javax.swing.JOptionPane;

public class Programa2Grau {

	public static void main(String[] args) {
		//Programa Equa��o de 2�GRAU
        int escolha = 0;
        double delta, x1, x2, a, b, c, xv, yv;
        do{
        	escolha=Integer.parseInt(JOptionPane.showInputDialog("Escolha uma das op��es:\n\n[1]Programa equa��o do 2� grau\n[2]About\n[3]Sair"));
        	switch(escolha){
        	case 1:
        		a=Integer.parseInt(JOptionPane.showInputDialog("Digite o valor de a"));
        		while(a==0){
        		a=Integer.parseInt(JOptionPane.showInputDialog("Valor inv�lido!\nDigite outro valor para a"));
        		}
        		b=Integer.parseInt(JOptionPane.showInputDialog("Digite o valor de b"));
        		c=Integer.parseInt(JOptionPane.showInputDialog("Digite o valor de c"));
                delta=Math.pow(b, 2)-4*a*c;
                xv=-b/(2*a);
                yv=-delta/(4*a);
                JOptionPane.showMessageDialog(null, "A cordenada cartesiana � xv="+xv+" yv="+yv);
        	}
        }while(escolha!=3);
	}

}