int right = 6; // we want to call the move function then reset so its only called when the key is pressed, not continously
int left = 7;
int forward = 9;
int backward = 8;

int time = 50;
int command = 0;

void setup() {
  pinMode(right, OUTPUT);
  pinMode(left, OUTPUT);
  pinMode(forward, OUTPUT);
  pinMode(backward, OUTPUT);
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void forward_func(int time){
  digitalWrite(forward, LOW);
  delay(time);
}

void right_func(int time){
  digitalWrite(right, LOW);
  delay(time);
}

void backward_func(int time){
  digitalWrite(backward, LOW);
  //command = 0;
  delay(time);
}

void left_func(int time){
  digitalWrite(left, LOW);
  delay(time);
}

void forward_right(int time){
  digitalWrite(forward, LOW);
  digitalWrite(right, LOW);
  delay(time);
}

void forward_left(int time){
  digitalWrite(forward, LOW);
  digitalWrite(left, LOW);
  delay(time);
}

void backward_right(int time){
  digitalWrite(backward, LOW);
  digitalWrite(right, LOW);
  delay(time);
}

void backward_left(int time){
  digitalWrite(backward, LOW);
  digitalWrite(left, LOW);
  delay(time);
}


void reset(){
  digitalWrite(right, HIGH);
  digitalWrite(left, HIGH);
  digitalWrite(forward, HIGH);
  digitalWrite(backward, HIGH);
}

void loop() {


  // put your main code here, to run repeatedly:
  
  
  if (Serial.available() > 0){
    command = Serial.read();
  }
  else{
    reset();
  }
    send_command(command,time);
}




void send_command(int command, int time){
  switch (command){
    case 0: reset(); break;

    case 1: forward_func(time); break;
    case 2: backward_func(time); break;
    case 3: right_func(time); break;
    case 4: left_func(time); break;

    case 5: forward_right(time); break;
    case 6: forward_left(time); break;
    case 7: backward_right(time); break;
    case 8: backward_left(time); break;

    default: Serial.print("Inalid Command\n");
  }
}


