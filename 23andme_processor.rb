f = IO.readlines("test_genome.txt")

total_same = 0
total_different = 0

f.each do |line|

	next if line[0] == "#"
		data = line.chomp().split("\t")

		next if data[1] == "MT"

			same = data[3][0] == data[3][1]

			if same
				total_same += 1
			else
				total_different += 1
			end
	end

	puts total_same
	puts total_different