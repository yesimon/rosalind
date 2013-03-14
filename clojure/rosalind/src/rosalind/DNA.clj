(ns rosalind.DNA
  (:gen-class))

(defn -main
  [& args]
  (let [freq (frequencies (read-line))]
    (printf "%d %d %d %d\n" (freq \A) (freq \C) (freq \G) (freq \T))))
