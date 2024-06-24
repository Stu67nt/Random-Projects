#include <LiquidCrystal.h>

// Defining all pins so program is more readable
#define pauseGame 0
#define addBonus 4
#define startEndGame 2
#define addOneSec 1
#define addOneMin 5
#define resetTimer 3
#define blackEndTurn 7
#define whiteEndTurn 6

// Defining all variables and constants program will use
bool timerMode = false;
unsigned int totalTime = 0;
unsigned int BlackTimeLeft = 0;
unsigned int WhiteTimeLeft = 0;
unsigned int bonusTime = 0;
unsigned int number = 0;
bool WhiteorBlack = true; // true = white	false = black
String emptySpace = "  ";
unsigned int Whours = 0;
unsigned int Wmins = 0;
unsigned int Wsecs = 0;
unsigned int Bhours = 0;
unsigned int Bmins = 0;
unsigned int Bsecs = 0;
unsigned int num = 0;
unsigned long runtime = 0; 
unsigned long currenttime = 0;
unsigned int isoverthousand = 0;
unsigned int numB = 0;
unsigned long runtimeB = 0; 
unsigned long currenttimeB = 0;
unsigned int isoverthousandB = 0;

// Telling LCD display which pins it is using
LiquidCrystal lcd(8, 9, 10, 11, 12, 13);

// Code only ran when the program initially boots
void setup() 
{
 lcd.begin(16,2);
 lcd.clear();
 
 // Defining all input devices such as buttons and switches
 pinMode(startEndGame,INPUT_PULLUP);
 pinMode(addOneSec, INPUT_PULLUP);   
 pinMode(addOneMin, INPUT_PULLUP);   
 pinMode(resetTimer, INPUT_PULLUP);   
 pinMode(addBonus, INPUT_PULLUP);
 pinMode(pauseGame, INPUT_PULLUP);
 pinMode(blackEndTurn, INPUT_PULLUP);
 pinMode(whiteEndTurn, INPUT_PULLUP);

 // Prints the main setup menu for the LCD to display
 lcd.print("Chess timer");
 lcd.setCursor(0,1);
 Wsecs = totalTime % 60;
 Wmins = totalTime / 60;
 Whours = totalTime / 3600;
 if (Wmins > 59){
 Wmins = Wmins-(Whours*60);
 }
      
 lcd.print(String(Whours)+":"+String(Wmins)+":"+String(Wsecs)+"  INC:"+String(bonusTime));
}

// This section will run continuously
void loop()
{
 
  //Setup mode - Section of code runs if not in game
  if (timerMode == false){ 
    
    // Adds one second to the total time players can have
    if(digitalRead(addOneSec) == LOW){
      if (totalTime < 32400){
      	totalTime = totalTime+1;
      }
      else{
      	totalTime = 32400;
      }
      
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("Chess timer:");
      lcd.setCursor(0,1);
      
      Wsecs = totalTime % 60;
      Wmins = totalTime / 60;
      Whours = totalTime / 3600;
      if (Wmins > 59){
      	Wmins = Wmins-(Whours*60);
      }
      
      lcd.print(String(Whours)+":"+String(Wmins)+":"+String(Wsecs)+"  INC:"+String(bonusTime));
      delay(200);
    }
   
    // Adds one miniute to the total time players can have
    if(digitalRead(addOneMin) == LOW){
      if (totalTime < 32400){
      	totalTime = totalTime+60;
      }
      else{
      	totalTime = 32400;
      }
      
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("Chess timer:");
      lcd.setCursor(0,1);
      
      Wsecs = totalTime % 60;
      Wmins = totalTime / 60;
      Whours = totalTime / 3600;
      if (Wmins > 59){
      	Wmins = Wmins-(Whours*60);
      }
      
      lcd.print(String(Whours)+":"+String(Wmins)+":"+String(Wsecs)+"  INC:"+String(bonusTime));
      delay(200);
    }

    // Sets total time a player can have to 0 seconds, 0 seconds bonus time
    if(digitalRead(resetTimer) == LOW){
      totalTime = 0;
      bonusTime = 0;
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("Chess timer:");
      lcd.setCursor(0,1);
      
      Wsecs = totalTime % 60;
      Wmins = totalTime / 60;
      Whours = totalTime / 3600;
      if (Wmins > 59){
      	Wmins = Wmins-(Whours*60);
      }
      
      lcd.print(String(Whours)+":"+String(Wmins)+":"+String(Wsecs)+"  INC:"+String(bonusTime));
      delay(200);
    }

    // Adds one second to players bonus time
    if (digitalRead(addBonus) == LOW){
      if (bonusTime < 90){	
      	bonusTime = bonusTime+1;
      }
      else{
        bonusTime = 90;
      }
    
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("Chess timer:");
      lcd.setCursor(0,1);
      
      Wsecs = totalTime % 60;
      Wmins = totalTime / 60;
      Whours = totalTime / 3600;
      if (Wmins > 59){
      	Wmins = Wmins-(Whours*60);
      }
      
      lcd.print(String(Whours)+":"+String(Wmins)+":"+String(Wsecs)+"  INC:"+String(bonusTime));
      delay(200);
    }
    
    // Starts the game
    if(digitalRead(startEndGame) == LOW & totalTime != 0){
      timerMode = true;
      BlackTimeLeft = totalTime;
      WhiteTimeLeft = totalTime;
      String (WhiteTimeLeft);
      String (BlackTimeLeft);
      delay(400);
    }
  }
  
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  
  
  // Gameplay Mode - Section of code runs when in a game.
  if (timerMode == true){
    
    // Section of code formats everything once the game starts and to get everything for new game
    if (number == 0){
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("White  ||  Black");
      number = number+1;
      Wsecs = totalTime % 60;
      Wmins = totalTime / 60;
      Whours = totalTime / 3600;
      if (Wmins > 59){
      	Wmins = Wmins-(Whours*60);
      }
      Bhours = Whours;
      Bmins = Wmins;
      Bsecs = Wsecs;
      WhiteorBlack = true;
    }
    
    // Formats LCD display for game mode and display.
    lcd.setCursor(0,1);
    lcd.print(String(Whours)+":"+String(Wmins)+":"+String(Wsecs)+"  ");
    lcd.setCursor(7,1);
    lcd.print("||"+ String(Bhours)+":"+String(Bmins)+":"+String(Bsecs)+"  ");
    
    // Checks if Whites end turn button has been pressed if true ends Whites turn and gives whites timer bonus time.
    if (digitalRead(whiteEndTurn) == LOW & WhiteorBlack == true){
      WhiteTimeLeft = WhiteTimeLeft+bonusTime;
      num = 0;
      currenttime = 0;
      runtime = 0;
      if (WhiteTimeLeft > 32601){
      	WhiteTimeLeft = 32601;
      } 
      WhiteorBlack = false;
      Wsecs = WhiteTimeLeft % 60;
      Wmins = WhiteTimeLeft / 60;
      Whours = WhiteTimeLeft / 3600;
      if (Wmins > 59){
      	Wmins = Wmins-(Whours*60);
      }
      
      lcd.setCursor(0,1);
      lcd.print(String(Whours)+":"+String(Wmins)+":"+String(Wsecs)+"  ");
      lcd.setCursor(7,1);
      lcd.print("||"+ String(Bhours)+":"+String(Bmins)+":"+String(Bsecs)+"  ");
    
    }
    
    // Checks if Blacks end turn button has been pressed if true ends Blacks turn and gives blacks timer bonus time.
    if (digitalRead(blackEndTurn) == LOW & WhiteorBlack == false){  
      numB = 0;
      currenttimeB = 0;
      runtimeB = 0;
      BlackTimeLeft = BlackTimeLeft+bonusTime;
      if (BlackTimeLeft > 32600){
      	BlackTimeLeft = 32600;
      } 
      WhiteorBlack = true;
      
      Bsecs = BlackTimeLeft % 60;
      Bmins = BlackTimeLeft / 60;
      Bhours = BlackTimeLeft / 3600;
      if (Bmins > 59){
      	Bmins = Bmins-(Bhours*60);
      }
      
      lcd.setCursor(0,1);
      lcd.print(String(Whours)+":"+String(Wmins)+":"+String(Wsecs)+"  ");
      lcd.setCursor(7,1);
      lcd.print("||"+ String(Bhours)+":"+String(Bmins)+":"+String(Bsecs)+"  ");
    
    }
  	
    // If Whites turn time remaining is reduced by 1 sec
    if (WhiteorBlack == true){
      if (num == 0){
      	runtime = millis();
        num = num+1;
      }
      
      if (num == 1){
        currenttime = millis();
        isoverthousand = currenttime - runtime;
        if (isoverthousand >= 1000){
        	num = num+1;
          	isoverthousand = 0;
        }
      }
      
      if (num == 2){
      	WhiteTimeLeft = WhiteTimeLeft-1;
        num = 0;
        currenttime = 0;
        runtime = 0;
      }
      
      Wsecs = WhiteTimeLeft % 60;
      Wmins = WhiteTimeLeft / 60;
      Whours = WhiteTimeLeft / 3600;
      if (Wmins > 59){
      	Wmins = Wmins-(Whours*60);
      }
    } 
    
    // If Blacks turn time remaining is reduced by 1 sec
    if (WhiteorBlack == false){
      if (numB == 0){
      	runtimeB = millis();
        numB = numB+1;
      }
      
      if (numB == 1){
        currenttimeB = millis();
        isoverthousandB = currenttimeB - runtimeB;
        if (isoverthousandB >= 1000){
        	numB = numB+1;
          	isoverthousandB = 0;
        }
      }
      
      if (numB == 2){
      	BlackTimeLeft = BlackTimeLeft-1;
        numB = 0;
        currenttimeB = 0;
        runtimeB = 0;
      }
      Bsecs = BlackTimeLeft % 60;
      Bmins = BlackTimeLeft / 60;
      Bhours = BlackTimeLeft / 3600;
      if (Bmins > 59){
      	Bmins = Bmins-(Bhours*60);
      }
    }
    
    // Checks to see if any players time has finished
    if ((WhiteTimeLeft <= 0)||(BlackTimeLeft <= 0)){
      
      // If Whites time is 0 then timer stops and timer ends game.
      if (WhiteTimeLeft <= 0){
      	lcd.clear();
      	lcd.setCursor(0,0);
      	lcd.print("White Time Up!");
        delay(2000);
      	timerMode = false;
      }
      
      // If Blacks time is 0 then timer stops and timer ends game.
      if (BlackTimeLeft <= 0){
        lcd.clear();
        lcd.setCursor(0,0);
      	lcd.print("Black Time Up!");
      	delay(2000);
      	timerMode = false;
      }
    }
    
    // Check to see if pauseGame switch is on
    while (digitalRead(pauseGame) == LOW){
      
      // Game is paused in this state until pauseGame Switch is off
      lcd.setCursor(0,0);
      lcd.print("Game Paused     ");
      
      // Check to see if startEndGame is pressed if it is then the game is ended and user is prompted to turn off pause to go back to setup mode.
      if (digitalRead(startEndGame) == LOW){
        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print("Game Ended");
        lcd.setCursor(0,1);
        lcd.print("Turn off pause");
        timerMode = false;
      }
    }
    
    lcd.setCursor(0,0);
    lcd.print("White  ||  Black");
    
    // Check to see if still in a game. 
    if (timerMode == false) {
      // Clears LCD display and displays the setup mode.
      number = 0;
      lcd.clear();
      WhiteTimeLeft = 0;
      lcd.print("Chess timer:");
      lcd.setCursor(0,1);
      Wsecs = totalTime % 60;
      Wmins = totalTime / 60;
      Whours = totalTime / 3600;
      if (Wmins > 59){
      	Wmins = Wmins-(Whours*60);
      }
      lcd.print(String(Whours)+":"+String(Wmins)+":"+String(Wsecs)+"  INC:"+String(bonusTime));
    }
  }
}