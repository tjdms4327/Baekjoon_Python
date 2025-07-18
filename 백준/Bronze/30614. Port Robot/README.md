# [Bronze I] Port Robot - 30614 

[문제 링크](https://www.acmicpc.net/problem/30614) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 자료 구조, 스택

### 제출 일자

2025년 1월 21일 19:32:07

### 문제 설명

<p>You are developing a robot that helps in storing containers that have arrived at ports before sending them to ships. These robots are responsible for handling these containers using limited space. Specifically, the space can fit multiple containers one over the other, but not side by side, as depicted in the figure.</p>

<p>While operating, the robot performs two actions:</p>

<ol>
	<li>Putting a container in storage.</li>
	<li>Taking a container from storage.</li>
</ol>

<p>There are 26 types of containers in this port, each one characterized by a letter of the Latin alphabet. Each time an action is performed, the robot logs the type of the container in lowercase when storing a container and in uppercase when taking a container from storage. Your task is to <u>check</u> if the logs produced by a robot indicate stable operation. In stable operation, the logged containers of action type 2 exist in storage and are in the uppermost position. Moreover, in stable operation, we always end with empty storage.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0c20ad0e-7ec0-47d4-b76f-1f8732535c06/-/preview/" style="width: 484px; height: 400px;"></p>

<p>As an example, consider a scenario in which the robot produces the log: 'cdDC'. Here, we have a stable operation of the robot, as the robot initially places 'c' and then 'd' (indicating that 'd' is in the upper position). The robot then takes the first 'd' out and, finally, takes out 'c'. On the other hand, an unstable operation would result from the log: 'cdCD', since the robot cannot take 'c' before taking out 'd'.</p>

### 입력 

 <p>The first line contains the length of the log generated by the robot. The second line contains the extracted log of the robot operation.</p>

### 출력 

 <p>A single number 0 if the log indicate wrong operation and 1 if the operation is stable.</p>

