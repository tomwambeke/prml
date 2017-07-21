class DataIO(object):
    """ Read/Write regression data to and from file

    WRITE
    - open file, write title
    - write each vector as a column to the file

    READ
    - open file, read title
    - read each column from the file, convert to vectors

    """
    
    @classmethod
    def write_data(cls, cols, file_name, title):
        """ Write vectors of data to file.

        :param cols - list of np arras of length N.
        :param file_name - str, name of the output file.
        :param title - str, header line (1)

        :output None - data is written to file.
        """
        with open(file_name, 'w') as f:
            f.write(title +' \n')

            if len(cols) > 1:
                seg = '{0:.5f}'
                for values in zip(*cols):
                    line = [seg.format(v) for v in values]
                    line = '\t'.join(line) + '\n'
                    f.write(line)
            elif len(cols) == 1:
                line = '{0:.5f}\n'
                for x in cols[0]:
                    line = line.format(x)
                    f.write(line)

    @classmethod
    def read_data(cls, file_name):
        """ Read vectors of data from file.

        :param file_name - str, name of the data file.

        :output data - list of vectors.
        """
        with open(file_name, 'r') as f:
            for i, line in enumerate(f):
                line = line.strip('\n')
                line = line.split('\t')
                if i == 0:
                    data = [[] for nvar in range(len(line))]
                else:
                    line = [float(x) for x in line]
                    for d, l in zip(data, line):
                        d.append(l)
        return data

