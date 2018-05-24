//Programa: Conectando Sensor Ultrassonico HC-SR04 ao Arduino
//Autor: FILIPEFLOP

//Carrega a biblioteca do sensor ultrassonico
#include <Ultrasonic.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
//Define os pinos para o trigger e echo
#define pino_trigger 7
#define pino_echo 6

//Inicializa o sensor nos pinos definidos acima
Ultrasonic ultrasonic(pino_trigger, pino_echo);

void setup()
{
  lcd.begin(16, 2);
  Serial.begin(9600);
  //Serial.println("Lendo dados do sensor...");
  
}

void loop()
{
  lcd.clear();
  //Le as informacoes do sensor, em cm e pol
  float cmMsecInit,cmMsecFim;
  long microsecInit,microsecFim;
  microsecInit = ultrasonic.timing();
  delay(800);
  microsecFim = ultrasonic.timing();
  delay(100);
  cmMsecInit = ultrasonic.convert(microsecInit, Ultrasonic::CM);
  cmMsecFim = ultrasonic.convert(microsecFim, Ultrasonic::CM);
  float velocidade = (cmMsecInit-cmMsecFim)/(0.8);
  
  if (cmMsecInit<50){
    if(cmMsecFim>4){
      if(velocidade >0){
      lcd.setCursor(0, 1);
      lcd.print(velocidade);
      lcd.print("cm/s");
      lcd.setCursor(0, 0);
      {
      if(velocidade>20.0){
      lcd.print("Acima!");
      delay(3000);
      }else {
         lcd.print("Esta ok!");
          delay(3000);
      //  Serial.print("Velocidade acima do limite");
    }}
  }}
  Serial.print("\n ");
  //Serial.println(inMsec);
  delay(1000);
}}
