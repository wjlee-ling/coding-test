# [unrated] 야간 전술보행 - 133501 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/133501) 

### 성능 요약

메모리: 10.5 MB, 시간: 15.38 ms

### 구분

코딩테스트 연습 > 연습문제

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p>전쟁에 참여한 화랑이는 적군의 기지에 침투하여 정보를 훔쳐오는 임무를 받았습니다. 화랑이는 야간 전술 보행을 이용하여 직진하며, 야간 전술 보행은 1m/s의 일정한 속도로 나아갈 수 있습니다. 화랑이의 침입 경로에는 경비병들이 각자 일부 구간들을 감시하고 있습니다. 각각의 경비병들이 감시하는 구간은 서로 겹치지 않으며, 일정 시간 동안 근무 후 일정 시간 동안 휴식을 취하는 과정을 반복합니다. 화랑이가 지나가고 있는 위치를 감시하는 경비병이 근무 중이라면 화랑이는 경비병에게 발각되어 즉시 붙잡히게 됩니다. 하지만 해당 위치를 감시하는 경비병이 휴식을 취하고 있으면 화랑이는 무사히 해당 위치를 지나갈 수 있습니다. 경비병의 근무 정보를 모르는 화랑이는 쉬지 않고 전진을 하며, 화랑이가 출발할 때 모든 경비병들이 동시에 근무를 시작합니다.</p>

<p>예를 들어, 적군 기지까지의 거리가 10m이고 2명의 경비병들이 근무를 시작한다고 가정합시다. 첫 번째 경비병의 감시 구간은 화랑이의 출발 위치로부터 3m부터 4m까지이고, 두 번째 경비병의 감시 구간은 화랑이의 출발 위치로부터 5m부터 8m까지입니다. 첫 번째 경비병의 근무 및 휴식 시간은 각각 2초, 5초를 반복하며, 두 번째 경비병의 근무 및 휴식 시간은 각각 4초, 3초를 반복합니다. 이 경우 출발지로부터 화랑이의 위치에 따른 두 경비병의 상태는 아래 표와 같습니다. 첫 번째 경비병이 감시하는 3m ~ 4m 구간을 화랑이는 3초일 때 진입하지만, 첫 번째 경비병은 2초간의 근무를 마치고, 휴식을 시작했으므로, 화랑이는 붙잡히지 않습니다. 하지만 두 번째 경비병이 감시하는 5m ~ 8m 구간에서 화랑이가 8m 지점에 진입했을 때, 두 번째 경비병이 3초간의 휴식을 마치고 근무를 시작하므로 화랑이는 붙잡히게 됩니다.</p>
<table class="table">
        <thead><tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
        <tbody><tr>
<td>첫 번째 경비병의 상태</td>
<td>근무</td>
<td>근무</td>
<td>휴식</td>
<td>휴식</td>
<td>휴식</td>
<td>휴식</td>
<td>휴식</td>
<td>근무</td>
<td>근무</td>
<td>휴식</td>
</tr>
<tr>
<td>두 번째 경비병의 상태</td>
<td>근무</td>
<td>근무</td>
<td>근무</td>
<td>근무</td>
<td>휴식</td>
<td>휴식</td>
<td>휴식</td>
<td>근무</td>
<td>근무</td>
<td>근무</td>
</tr>
<tr>
<td>화랑이의 위치</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>10</td>
</tr>
</tbody>
      </table>
<p>화랑이의 현재 위치와 적군 기지 사이의 거리를 나타내는 정수 <code>distance</code>, 각 경비병의 감시 구간을 담은 2차원 정수 배열 <code>scope</code>, 같은 순서로 각 경비병의 근무 시간과 휴식 시간을 담은 2차원 정수 배열 <code>times</code>가 주어질 때, 화랑이가 경비를 피해 최대로 이동할 수 있는 거리를 return 하는 solution 함수를 완성하세요.</p>

<hr>

<h5>제한사항</h5>

<ul>
<li>10 ≤ <code>distance</code> ≤ 10,000,000</li>
<li>1 ≤ <code>scope</code>의 길이, <code>times</code>의 길이 ≤ 1,000

<ul>
<li><code>scope[i]</code>는 i+1번째 경비병이 감시하는 구간입니다.

<ul>
<li><code>scope[i]</code>를 [a, b]라고 했을 때, (a ≠ b)입니다.</li>
<li><code>scope[i]</code>는 정렬되어 있지 않을 수 있습니다(예시 2번 참조).</li>
</ul></li>
<li>경비병의 감시구간은 서로 겹치지 않습니다.</li>
<li>1 ≤ <code>scope</code>의 원소 ≤ distance</li>
<li>1 ≤ <code>times</code>의 원소 ≤ 10</li>
<li><code>times[i]</code>는 i+1번째 경비병의 [근무 시간, 휴식 시간]입니다.</li>
</ul></li>
</ul>

<hr>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>distance</th>
<th>scope</th>
<th>times</th>
<th>result</th>
</tr>
</thead>
        <tbody><tr>
<td>10</td>
<td>[[3, 4], [5, 8]]</td>
<td>[[2, 5], [4, 3]]</td>
<td>8</td>
</tr>
<tr>
<td>12</td>
<td>[[7, 8], [4, 6], [11, 10]]</td>
<td>[[2, 2], [2, 4], [3, 3]]</td>
<td>12</td>
</tr>
</tbody>
      </table>
<hr>

<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<ul>
<li>문제 예시와 같습니다.</li>
</ul>

<p><strong>입출력 예 #2</strong></p>

<ul>
<li>아래의 표는 화랑이의 위치에 따른 세 경비병의 상태를 보여줍니다. 첫 번째 경비병이 감시하는 7m ~ 8m 구간을 화랑이가 지날 때, 첫 번째 경비병은 휴식 중입니다. 두 번째 경비병이 감시하는 4m ~ 6m 구간을 화랑이가 지날 때, 두 번째 경비병은 휴식 중입니다. 세 번째 경비병이 감시하는 10m ~ 11m 구간을 화랑이가 지날 때, 세 번째 경비병은 휴식 중입니다. 따라서 화랑이가 무사히 적군 기지에 침투할 수 있으므로 적군 기지까지의 거리인 12을 return 합니다.</li>
</ul>
<table class="table">
        <thead><tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
        <tbody><tr>
<td>첫 번째 경비병의 상태</td>
<td>근무</td>
<td>근무</td>
<td>휴식</td>
<td>휴식</td>
<td>근무</td>
<td>근무</td>
<td>휴식</td>
<td>휴식</td>
<td>근무</td>
<td>근무</td>
<td>휴식</td>
<td>휴식</td>
</tr>
<tr>
<td>두 번째 경비병의 상태</td>
<td>근무</td>
<td>근무</td>
<td>휴식</td>
<td>휴식</td>
<td>휴식</td>
<td>휴식</td>
<td>근무</td>
<td>근무</td>
<td>휴식</td>
<td>휴식</td>
<td>휴식</td>
<td>휴식</td>
</tr>
<tr>
<td>세 번째 경비병의 상태</td>
<td>근무</td>
<td>근무</td>
<td>근무</td>
<td>휴식</td>
<td>휴식</td>
<td>휴식</td>
<td>근무</td>
<td>근무</td>
<td>근무</td>
<td>휴식</td>
<td>휴식</td>
<td>휴식</td>
</tr>
<tr>
<td>화랑이의 위치</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
<td>7</td>
<td>8</td>
<td>9</td>
<td>10</td>
<td>11</td>
<td>12</td>
</tr>
</tbody>
      </table>

> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges