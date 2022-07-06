
package entities;

/**
 *
 * @author Bruno
 */
public class Disciplina {
    private String nome;
    private float nota1;
    private float nota2;
    private float media;

    public Disciplina(String nome, float nota1, float nota2, float media) {
        this.nome = nome;
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.media = media;
    }

    public Disciplina() {
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public float getNota1() {
        return nota1;
    }

    public void setNota1(float nota1) {
        this.nota1 = nota1;
    }

    public float getNota2() {
        return nota2;
    }

    public void setNota2(float nota2) {
        this.nota2 = nota2;
    }

    public float getMedia() {
        return media;
    }

    public void setMedia(float media) {
        this.media = media;
    }
    
    @Override
    public String toString(){
        return "\n--------------------------\nNome: " + nome
                +"\nNota 1: " + nota1
                +"\nNota 2: " + nota2
                +"\nMedia: " + media;
    }
}
