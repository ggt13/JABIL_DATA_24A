clear all;
%a = serialport('COM5',9600); %configura el puerto
a = arduino;
valuePot1='A0';
k=0:11;

for k=0:1:11;
    lectura = readVoltage(a,valuePot1);
    %disp(lectura);
    pause();
    %k=k+1; 
    %datos(k)=lectura
    A=[k,valuePot1]
end

B=A.'
