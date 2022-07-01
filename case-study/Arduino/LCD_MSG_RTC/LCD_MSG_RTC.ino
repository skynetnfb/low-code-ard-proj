#include <LiquidCrystal.h>
#include <Wire.h>
#include <SimpleDHT.h>
#include "RTClib.h"

SimpleDHT11 dht11;
const int rs=12, en=11, d4=5, d5=4, d6=3, d7=2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
RTC_DS1307 rtc;

void setup() {
  pinMode(13,OUTPUT);
  lcd.begin(16,2);
  //lcd.print("Time & Weather");
  
  Serial.begin(9600);
  if(!rtc.begin()){
    lcd.print("RTC Error!");
    return;
    }
  if(DateTime(F(__DATE__),F(__TIME__))!= rtc.now()){
    rtc.adjust(DateTime(F(__DATE__),F(__TIME__)));
    }

}

void loop() {
 byte temp = 0;
 byte hum = 0;
 int err = SimpleDHTErrSuccess;
 if((err = dht11.read(6,&temp,&hum,NULL))!=SimpleDHTErrSuccess){
  lcd.setCursor(0,9);
  //lcd.print("DHT11 Error!");
  Serial.println(err);
  delay(1000);
  return;
  }
  
 DateTime now = rtc.now();
 lcd.setCursor(1,0);

 
  //lcd.print(now.year(),DEC);
  //lcd.print("/");
  //lcd.print(pad(now.month()));
  //lcd.print("/");
  //lcd.print(pad(now.day()));
  //lcd.print("/");
  lcd.print(pad(now.hour()));
  lcd.print(":");
  lcd.print(pad(now.minute()));
  lcd.print(":");
  lcd.print(pad(now.second()));
  lcd.setCursor(0,9);
  lcd.print(" T:");
  lcd.print((int)temp);
  lcd.print(" C");
  lcd.print(" H");
  lcd.print((int)hum);
  lcd.print("%");
  if((int)hum > 70){
  digitalWrite(13,HIGH);
  }else{
    digitalWrite(13,LOW);
    }
 delay(1000);
 
}

//memory allocation of 5 byte 
char *res = malloc(5);

String pad(int n){
  sprintf(res, "%02d", n);
  // "%02d" formatta una stringa di lunghezza 1 in una di lunghezza 2
  return String(res);
  }
