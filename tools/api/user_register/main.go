package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	_ "crypto/sha256" // https://github.com/Kong/go-srp/issues/1

	argparser "github.com/alexflint/go-arg"
	"github.com/kong/go-srp"
	"github.com/mazen160/go-random"
)

var args struct {
	Username string `arg:"required"`
	Password string `arg:"required"`
	Host     string `default:"127.0.0.1"`
	Port     string `default:"3000"`
}

type Register_Payload struct {
	Username     string `json:"username"`
	Srp_verifier string `json:"srp_verifier"`
	Srp_salt     string `json:"srp_salt"`
}

func gen_srp_vkey(username string, password string) ([]uint8, []byte) {

	salt, err := random.Bytes(4)
	if err != nil {
		log.Fatal("Error while generating salt...")
	}
	srp_params := srp.GetParams(2048)

	verifier := srp.ComputeVerifier(srp_params, salt, []byte(args.Username), []byte(args.Password))
	return verifier, salt
}

func main() {
	argparser.MustParse(&args)

	vkey, srp_salt := gen_srp_vkey(args.Username, args.Password)
	srp_salt_str := base64.RawStdEncoding.EncodeToString(srp_salt)
	srp_vkey_str := base64.RawStdEncoding.EncodeToString(vkey)

	rq_payload := Register_Payload{
		Username:     args.Username,
		Srp_verifier: srp_vkey_str,
		Srp_salt:     srp_salt_str,
	}

	rq_payload_json, err := json.Marshal(rq_payload)
	if err != nil {
		log.Fatal("Error while JSON-encoding payload...")
	}
	http_formatted_payload := bytes.NewBuffer(rq_payload_json)

	http_url := "http://" + args.Host + ":" + args.Port + "/register"
	resp, err := http.Post(http_url, "application/json", http_formatted_payload)
	if err != nil {
		log.Fatal("Something happened while making POST request to the API.")
	}
	defer resp.Body.Close()

	switch resp.StatusCode {
	case 400:
		log.Fatal("Bad request.")
	case 201:
		fmt.Println("User successfully registered!")
	case 409:
		fmt.Println("User already exists")
	default:
		log.Fatalf("Unandled status code %v", resp.StatusCode)
	}
}
