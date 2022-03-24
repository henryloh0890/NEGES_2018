//import lingscope.drivers.*;
//import abner.Tagger;
import abner.Trainer;


public class train{

    public static void main(String[] args) {
        // Prints "Hello, World" to the terminal window.
	//SentenceTagger st = new SentenceTagger();
        //System.out.println("Hello, World");
	//String[] param = {"cue","crf","crf_cue_all_clinical.model","No radiographic abnormality seen of the chest."};
	//st.main(param);
	//ModelTrainer mt = new ModelTrainer();
	//String[] paramfortrain = {"cue","crf","allonlyneginBIO_c.txt", "allonlyneg_cue.model"};
	//mt.main(paramfortrain);
	
	Trainer trainer = new Trainer();
	trainer.train("neges_train_task2_inBIO3.txt", "neges_train_all3_1.model");
	
    }

}
