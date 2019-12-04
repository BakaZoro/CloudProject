# CloudProject

Simulation of how Federated Computing works across Multiple Clouds

𝐎𝐯𝐞𝐫𝐚𝐥𝐥 𝐟𝐮𝐧𝐜𝐭𝐢𝐨𝐧𝐢𝐧𝐠:

A program is run on a single cloud first and when the CPU utilisation in the VM in that cloud goes beyond a threshold value then the program simulaneoulsy starts on another VM in another Cloud. This way using cloud services provided by different cloud service providers, we make best use of the advantages and the services that different service providers have to offer. 


𝐃𝐞𝐭𝐚𝐢𝐥𝐬:

1. A program in "𝐂𝐥𝐨𝐮𝐝𝟏.𝐩𝐲" that counts the frequency of a number of words is run on a particular cloud instance first. 
2. A very big text file "𝐭𝐞𝐱𝐭𝐭𝐨𝐛𝐞𝐫𝐮𝐧" is given as input.
3. While the program runs on the first cloud instance, a shell script within the file monitors the CPU and Memory usage of that particular Virtual Machine.
4. When the overall statistics go beyond a threshold value, the program on the first instance is stopped and the same program ,i.e "𝐂𝐥𝐨𝐮𝐝𝟐.𝐩𝐲" is started which runs the program from where it was stopped using data acquired by pointer, in the second cloud instance.
5. The program then runs on the second cloud until the completion of the program.














Note: Due to unavailabity to obtain accounts of different cloud service providers (Azure/GCP), simulation using instances from a single cloud service provider has been used.



